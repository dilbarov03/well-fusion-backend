from django.db import models
from django.utils import timezone

from apps.common.models import BaseModel


class Plan(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    days_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"


class Subscription(BaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="subscription")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="subscriptions")
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    gym = models.ForeignKey("partners.Gym", on_delete=models.CASCADE, related_name="subscriptions",
                            null=True, blank=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
        unique_together = ("user", "plan")

    def __str__(self):
        return f"{self.user} - {self.plan}"

    @property
    def is_active(self):
        return self.start_date and self.end_date and self.start_date <= timezone.now() <= self.end_date


class Payment(models.Model):
    class Status(models.TextChoices):
        DRAFT = "Draft", "Draft"
        BLOCKED = "Blocked", "Blocked"
        CAPTURED = "Captured", "Captured"
        REFUNDED = "Refunded", "Refunded"
        PARTIALLY_REFUNDED = "PartiallyRefunded", "Partially Refunded"
        REJECTED = "Rejected", "Rejected"

    source = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=255, unique=True, db_index=True)
    type = models.CharField(max_length=50)
    sandbox = models.BooleanField(default=False)
    payment_status = models.CharField(max_length=50, choices=Status.choices)
    amount = models.FloatField()
    final_amount = models.FloatField(null=True, blank=True)
    currency = models.CharField(max_length=10)
    commission = models.FloatField(null=True, blank=True)
    preauthorized = models.BooleanField(default=False)
    can_be_captured = models.BooleanField(default=False)
    create_date = models.DateTimeField()
    capture_date = models.DateTimeField(null=True, blank=True)
    block_date = models.DateTimeField(null=True, blank=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    card_mask = models.CharField(max_length=20, null=True, blank=True)
    card_brand = models.CharField(max_length=50, null=True, blank=True)
    card_holder = models.CharField(max_length=255, null=True, blank=True)
    expiration_date = models.CharField(max_length=10, null=True, blank=True)
    secure_card_id = models.CharField(max_length=255, null=True, blank=True)
    rejection_reason = models.CharField(max_length=255, null=True, blank=True)

    refundable = models.BooleanField(default=False)
    refund_status = models.CharField(max_length=50, null=True, blank=True)
    refund_id = models.CharField(max_length=255, null=True, blank=True)
    refund_amount = models.FloatField(null=True, blank=True)
    refund_requested_amount = models.FloatField(null=True, blank=True)
    refund_reject_reason = models.CharField(max_length=255, null=True, blank=True)
    refund_date = models.DateTimeField(null=True, blank=True)

    # for OFD
    product_name = models.CharField(max_length=255, null=True, blank=True)
    product_code = models.CharField(max_length=255, null=True, blank=True)
    package_code = models.CharField(max_length=255, null=True, blank=True)
    product_quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    sum_price = models.FloatField(null=True, blank=True)
    vat = models.FloatField(null=True, blank=True)
    vat_percent = models.FloatField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # relations
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f'Payment {self.payment_id} - {self.payment_status}'

