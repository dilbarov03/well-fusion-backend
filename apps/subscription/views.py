from rest_framework import generics
from rest_framework.response import Response

from apps.subscription.models import Plan
from apps.subscription.serializers import PlanSerializer, PromoCodeSerializer
from apps.subscription.utils import generate_paylink


class PlanListAPIView(generics.ListAPIView):
    """List all plans."""

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class CheckoutAPIView(generics.GenericAPIView):
    """Create checkout session to pay for a plan. You can send promo code to get discount."""
    serializer_class = PromoCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        promo_code = serializer.validated_data.get("promo_code")
        payment_link = generate_paylink(subscription=request.user.subscription, promo_code=promo_code)
        return Response(payment_link)
