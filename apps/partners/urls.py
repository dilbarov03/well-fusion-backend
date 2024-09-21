from django.urls import path

from apps.partners.views import GymListAPIView, CatererListAPIView, CatererDetailAPIView

urlpatterns = [
    path("gym/", GymListAPIView.as_view(), name="gym-list"),
    path("caterer/", CatererListAPIView.as_view(), name="caterer-list"),
    path("caterer/<int:pk>/", CatererDetailAPIView.as_view(), name="caterer-detail")
]
