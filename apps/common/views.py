from rest_framework import generics

from apps.common.models import Message
from apps.common.serializers import MessageSerializer


class MessageAPIView(generics.CreateAPIView):
    """API endpoint for receiving messages from users."""
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
