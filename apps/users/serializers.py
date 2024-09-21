from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "email", "password", "subscription_from", "subscription_to",
            "is_pro_user"
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "is_pro_user": {"read_only": True},
            "subscription_from": {"read_only": True},
            "subscription_to": {"read_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
