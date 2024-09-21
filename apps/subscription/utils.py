import os
from datetime import timezone, timedelta

import requests

from apps.partners.models import Gym


def generate_paylink(subscription, plan, promo_code=None):
    payment_amount = float(plan.price)
    gym = None
    if promo_code:
        # give 10% discount
        payment_amount = payment_amount * 0.9
        gym = Gym.objects.get(promo_code=promo_code)

    headers = {
        "Content-Type": "application/json",
        "Authorization": os.getenv("PAYZE_AUTH_TOKEN")
    }

    request_data = {
        "source": "Card",
        "amount": payment_amount,
        "currency": "USD",
        "language": "EN",
        "hooks": {
            "webhookGateway": os.getenv("PAYZE_WEBHOOK_URL"),
            "successRedirectGateway": os.getenv("PAYZE_SUCCESS_URL"),
            "errorRedirectGateway": os.getenv("PAYZE_ERROR_URL")
        },
        "metadata": {
            "Order": {
                "OrderId": str(subscription.id),
                "OrderItems": None,
                "BillingAddress": None
            },
            "extraAttributes": [
                {
                    "key": "RECEIPT_TYPE",
                    "value": "Sale",
                    "description": "OFD Receipt type"
                },
                {
                    "key": "plan_id",
                    "value": str(plan.id),
                },
                {
                    "key": "gym_id",
                    "value": str(gym.id) if gym else None,
                }
            ]
        }
    }

    response = requests.put(
        "https://payze.io/v2/api/payment",
        headers=headers,
        json=request_data
    )

    response_data = response.json()

    if response.status_code != 200:
        return {
            "error": response_data
        }

    payment_url = response_data['data']['payment']['paymentUrl']

    return {
        "pay_link": payment_url
    }

def parse_iso_date(iso_string: str, target_timezone="+05:00"):
    from dateutil import parser

    dt_object = parser.isoparse(iso_string)

    # If the original timestamp is naive (no timezone info), assume UTC
    if dt_object.tzinfo is None:
        dt_object = dt_object.replace(tzinfo=timezone.utc)

    # Create a timezone object for the target timezone
    target_tz = timezone(timedelta(hours=int(target_timezone[:3]), minutes=int(target_timezone[4:])))

    # Convert to the target timezone
    return dt_object.astimezone(target_tz)


def get_payment_data(webhook_data: dict) -> dict:
    """Extracts and maps payment data from the webhook to a format suitable for the Payment model."""

    payment_data = {
        "source": webhook_data["Source"],
        "payment_id": webhook_data["PaymentId"],
        "type": webhook_data["Type"],
        "sandbox": webhook_data["Sandbox"],
        "payment_status": webhook_data["PaymentStatus"],
        "amount": webhook_data["Amount"],
        "final_amount": webhook_data.get("FinalAmount"),
        "currency": webhook_data["Currency"],
        "commission": webhook_data.get("Commission"),
        "preauthorized": webhook_data["Preauthorized"],
        "can_be_captured": webhook_data["CanBeCaptured"],
        "create_date": parse_iso_date(webhook_data["CreateDateIso"]),
        "capture_date": parse_iso_date(webhook_data["CaptureDateIso"]) if webhook_data.get("CaptureDateIso") else None,
        "block_date": parse_iso_date(webhook_data["BlockDateIso"]) if webhook_data.get("BlockDateIso") else None,
        "token": webhook_data.get("Token"),
        "card_mask": webhook_data.get("CardMask"),
        "card_brand": webhook_data.get("CardBrand"),
        "card_holder": webhook_data.get("CardHolder"),
        "expiration_date": webhook_data.get("ExpirationDate"),
        "secure_card_id": webhook_data.get("SecureCardId"),
        "rejection_reason": webhook_data.get("RejectionReason"),
    }

    # Extract Refund data (if available)
    refund_data = webhook_data.get("Refund")
    if refund_data:
        payment_data["refundable"] = refund_data.get("Refundable", False)
        payment_data["refund_status"] = refund_data.get("Status")
        payment_data["refund_id"] = refund_data.get("RefundId")
        payment_data["refund_amount"] = refund_data.get("Amount")
        payment_data["refund_requested_amount"] = refund_data.get("RequestedAmount")
        payment_data["refund_reject_reason"] = refund_data.get("RejectReason")
        if refund_data.get("RefundDateIso"):
            payment_data["refund_date"] = parse_iso_date(refund_data["RefundDateIso"])

    # Extract OFD data (if available)
    metadata = webhook_data.get("Metadata")
    if metadata and metadata.get("Order") and metadata["Order"].get("OrderItems"):
        order_item = metadata["Order"]["OrderItems"][0]  # Assuming only one item
        payment_data["product_name"] = order_item.get("ProductName")
        payment_data["product_code"] = order_item.get("ProductCode")
        payment_data["package_code"] = order_item.get("PackageCode")
        payment_data["product_quantity"] = order_item.get("ProductQuantity")
        payment_data["price"] = order_item.get("Price")
        payment_data["sum_price"] = order_item.get("SumPrice")
        payment_data["vat"] = order_item.get("Vat")
        payment_data["vat_percent"] = order_item.get("VatPercent")

    # Extract phone number from BillingAddress (if available)
    if metadata and metadata.get("Order") and metadata["Order"].get("BillingAddress"):
        payment_data["phone_number"] = metadata["Order"]["BillingAddress"].get("PhoneNumber")

    plan_id = next((item["Value"] for item in metadata["ExtraAttributes"] if item["Key"] == "plan_id"), None)
    gym_id = next((item["Value"] for item in metadata["ExtraAttributes"] if item["Key"] == "gym_id"), None)
    payment_data["plan_id"] = plan_id
    payment_data["gym_id"] = gym_id

    return payment_data


def refund_payment(payment):
    if not payment:
        return {
            "error": "Payment not found"
        }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': os.getenv('PAYZE_AUTH_TOKEN')  # API_KEY:API_SECRET
    }

    req_body = {
        "transactionId": payment.payment_id,
        "amount": payment.final_amount,
        "orderData": {
            "orderId": str(payment.order.id),
            "advanceContractId": "",
            "orderItems": None,
            "billingAddress": None,
        },
        "extraAttributes": [
            {
                "key": "RECEIPT_TYPE",
                "value": "Refund",
                "description": "OFD Receipt type"
            }
        ]
    }

    response = requests.put(
        "https://payze.io/v2/api/payment/refund",
        headers=headers,
        json=req_body
    )

    response_data = response.json()

    return response_data
