from django.urls import path

from apps.subscription.views import PlanListAPIView, CheckoutAPIView

urlpatterns = [
    path("plans/", PlanListAPIView.as_view(), name="plans"),
    path("checkout/", CheckoutAPIView.as_view(), name="checkout"),
]