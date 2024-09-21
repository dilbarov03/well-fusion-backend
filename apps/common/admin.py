from django.contrib import admin

from apps.common.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "created_at")
