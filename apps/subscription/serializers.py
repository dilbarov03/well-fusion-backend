from rest_framework import serializers

from apps.partners.models import Gym
from apps.subscription.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ("id", "name", "price", "days_count")


class CheckoutSerializer(serializers.Serializer):
    promo_code = serializers.CharField(required=False, allow_null=True)
    plan = serializers.PrimaryKeyRelatedField(queryset=Plan.objects.all())

    def validate_promo_code(self, value):
        if value and not Gym.objects.filter(promo_code=value).exists():
            raise serializers.ValidationError("Invalid promo code")
        return value
