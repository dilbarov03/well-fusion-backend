from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    list_display = ('id', 'email', 'first_name', 'last_name')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'first_name', 'last_name')
    list_per_page = 25

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )