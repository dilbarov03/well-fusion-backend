from rest_framework import serializers

from apps.partners.models import Gym


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ("id", "name", "promo_code")
