from django.contrib import admin

from .models import Plan, Subscription


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price')
    list_per_page = 25


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan', 'start_date', 'end_date', 'is_active')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'plan', 'start_date', 'end_date')
    list_filter = ('plan', 'user', 'is_active')
    list_per_page = 25

