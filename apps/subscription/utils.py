import os
import requests

def generate_paylink(subscription):
    payment_amount = float(subscription.plan.price)
    if subscription.gym:
        # give 10% discount
        payment_amount = payment_amount * 0.9

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
                "OrderId": subscription.id,
                "OrderItems": None,
                "BillingAddress": None
            },
            "extraAttributes": [
                {
                    "key": "RECEIPT_TYPE",
                    "value": "Sale",
                    "description": "OFD Receipt type"
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
