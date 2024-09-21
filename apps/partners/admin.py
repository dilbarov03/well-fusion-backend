from django.contrib import admin

from apps.partners.models import Gym


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "promo_code")
    search_fields = ("name", "promo_code")
    ordering = ("name",)
