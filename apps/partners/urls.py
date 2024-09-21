from django.urls import path

from apps.partners.views import GymListAPIView, CatererListAPIView

urlpatterns = [
    path("gym/", GymListAPIView.as_view(), name="gym-list"),
    path("caterer/", CatererListAPIView.as_view(), name="caterer-list"),
]
