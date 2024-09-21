from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import RegisterAPIView, MyProfileAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("profile/", MyProfileAPIView.as_view(), name="profile"),
]
