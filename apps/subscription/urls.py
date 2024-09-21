from django.urls import path

from apps.subscription.views import PlanListAPIView

urlpatterns = [
    path("plans/", PlanListAPIView.as_view(), name="plans"),
]