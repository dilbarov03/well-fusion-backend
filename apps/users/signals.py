from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.subscription.models import Subscription, Plan
from apps.users.models import User


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        plan = Plan.objects.get_or_create(
            name="Basic",
            price=0,
            description="Basic plan with a free trial",
            days_count=15
        )[0]
        Subscription.objects.create(
            user=instance,
            plan=plan,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=plan.days_count),
            is_active=True
        )
