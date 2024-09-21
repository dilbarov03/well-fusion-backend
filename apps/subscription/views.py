from django.db import transaction
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.subscription.models import Plan, Subscription, Payment
from apps.subscription.payment_serializers import PayzeWebhookSerializer
from apps.subscription.serializers import PlanSerializer, CheckoutSerializer
from apps.subscription.utils import generate_paylink, get_payment_data


class PlanListAPIView(generics.ListAPIView):
    """List all plans."""
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None


class CheckoutAPIView(generics.GenericAPIView):
    """Create checkout session to pay for a plan. You can send promo code to get discount."""
    serializer_class = CheckoutSerializer
    permission_classes = (IsAuthenticated,)


    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        promo_code = serializer.validated_data.get("promo_code")
        plan = serializer.validated_data.get("plan")
        payment_link = generate_paylink(subscription=request.user.subscription, plan=plan, promo_code=promo_code)
        return Response(payment_link)


class PayzeWebhookAPIView(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        serializer = PayzeWebhookSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        payment_data = get_payment_data(request.data)
        payment_status = validated_data["PaymentStatus"]

        order_id = validated_data["Metadata"]["Order"]["OrderId"]
        subscription = Subscription.objects.filter(id=order_id).first()

        if not subscription:
            return

        try:
            with transaction.atomic():
                if payment_status == "Captured":
                    plan_id = payment_data.pop("plan_id")
                    plan = Plan.objects.get(id=plan_id)
                    Subscription.objects.filter(user=subscription.user).update(
                        is_active=True,
                        plan_id=plan_id,
                        start_date=timezone.now(),
                        end_date=timezone.now() + timezone.timedelta(days=plan.days_count),
                        gym_id=payment_data.pop("gym_id")
                    )
                    Payment.objects.create(
                        user=subscription.user, subscription=subscription,
                        **payment_data
                    )

        except Exception as e:
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Webhook received successfully"}, status=status.HTTP_200_OK)
