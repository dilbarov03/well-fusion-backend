from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.serializers import UserSerializer


class RegisterAPIView(generics.CreateAPIView):
    """Register a new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class MyProfileAPIView(generics.RetrieveUpdateAPIView):
    """Retrieve and update the authenticated user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
