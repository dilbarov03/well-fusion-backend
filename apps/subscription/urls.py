from django.urls import path

from apps.subscription.views import PlanListAPIView, CheckoutAPIView, PayzeWebhookAPIView

urlpatterns = [
    path("plans/", PlanListAPIView.as_view(), name="plans"),
    path("checkout/", CheckoutAPIView.as_view(), name="checkout"),
    path("webhook/", PayzeWebhookAPIView.as_view(), name="webhook"),
]