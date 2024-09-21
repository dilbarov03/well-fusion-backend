from rest_framework import serializers

from apps.common.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "full_name", "phone", "text")
