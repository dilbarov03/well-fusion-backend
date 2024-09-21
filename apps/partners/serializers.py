from rest_framework import serializers

from apps.partners.models import Gym, Caterer, CatererMenu


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ("id", "name", "promo_code")


class CatererMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatererMenu
        fields = ("id", "name", "ingredients", "image", "price")


class CatererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caterer
        fields = ("id", "name", "location", "working_hours", "phone")


class CatererDetailSerializer(serializers.ModelSerializer):
    menus = CatererMenuSerializer(many=True)

    class Meta:
        model = Caterer
        fields = ("id", "name", "location", "working_hours", "phone", "menus")
