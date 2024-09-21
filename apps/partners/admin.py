from django.contrib import admin

from apps.partners.models import Gym, Caterer, CatererMenu


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "promo_code")
    search_fields = ("name", "promo_code")
    ordering = ("name",)


class CatererMenuInline(admin.StackedInline):
    model = CatererMenu
    extra = 0


@admin.register(Caterer)
class CatererAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "working_hours", "phone")
    search_fields = ("name", "location", "working_hours", "phone")
    ordering = ("name",)
    inlines = (CatererMenuInline,)
