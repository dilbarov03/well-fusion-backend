from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "email", "password", "subscription_from", "subscription_to",
            "is_subscribed"
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "is_subscribed": {"read_only": True},
            "subscription_from": {"read_only": True},
            "subscription_to": {"read_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
