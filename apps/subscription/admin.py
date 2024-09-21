from django.contrib import admin

from .models import Plan, Subscription, Payment


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
    list_filter = ('plan', 'user')
    list_per_page = 25


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'payment_id', 'type', 'payment_status', 'amount')
    list_display_links = ('id', 'source')
    search_fields = ('source', 'payment_id', 'type', 'payment_status', 'amount')
    list_filter = ('type', 'payment_status')
    list_per_page = 25
