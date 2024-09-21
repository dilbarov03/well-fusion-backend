from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from apps.common.models import BaseModel
from apps.users.managers import CustomUserManager


class User(AbstractUser, BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    subscription_from = models.DateTimeField(null=True, blank=True)
    subscription_to = models.DateTimeField(null=True, blank=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email

    @property
    def is_subscribed(self):
        return self.subscription_to and self.subscription_to > timezone.now()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.subscription_from = timezone.now()
            self.subscription_to = timezone.now() + timezone.timedelta(days=15)
        super().save(*args, **kwargs)
