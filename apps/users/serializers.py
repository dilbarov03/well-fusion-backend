from rest_framework import serializers

from apps.users.models import User


class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    is_active = serializers.BooleanField(read_only=True)
    plan = serializers.SerializerMethodField()

    def get_plan(self, instance):
        return instance.plan.name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "first_name", "last_name", "email", "password", "subscription"
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "subscription": {"read_only": True}
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if hasattr(instance, "subscription"):
            response["subscription"] = SubscriptionSerializer(instance.subscription).data
        else:
            response["subscription"] = None
        return response

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
