from django.urls import path

from apps.common.views import MessageAPIView

urlpatterns = [
    path("message/", MessageAPIView.as_view()),
]