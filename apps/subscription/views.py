from rest_framework import generics

from apps.subscription.models import Plan
from apps.subscription.serializers import PlanSerializer


class PlanListAPIView(generics.ListAPIView):
    """List all plans."""

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class CheckoutAPIView(generics.GenericAPIView):
    """Checkout plan."""

    def post(self, request):
        pass
