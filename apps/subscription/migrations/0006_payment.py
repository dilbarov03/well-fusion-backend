# Generated by Django 4.0.6 on 2024-09-21 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0005_alter_subscription_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('payment_id', models.CharField(db_index=True, max_length=255, unique=True)),
                ('type', models.CharField(max_length=50)),
                ('sandbox', models.BooleanField(default=False)),
                ('payment_status', models.CharField(choices=[('Draft', 'Draft'), ('Blocked', 'Blocked'), ('Captured', 'Captured'), ('Refunded', 'Refunded'), ('PartiallyRefunded', 'Partially Refunded'), ('Rejected', 'Rejected')], max_length=50)),
                ('amount', models.FloatField()),
                ('final_amount', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(max_length=10)),
                ('commission', models.FloatField(blank=True, null=True)),
                ('preauthorized', models.BooleanField(default=False)),
                ('can_be_captured', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField()),
                ('capture_date', models.DateTimeField(blank=True, null=True)),
                ('block_date', models.DateTimeField(blank=True, null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
                ('card_mask', models.CharField(blank=True, max_length=20, null=True)),
                ('card_brand', models.CharField(blank=True, max_length=50, null=True)),
                ('card_holder', models.CharField(blank=True, max_length=255, null=True)),
                ('expiration_date', models.CharField(blank=True, max_length=10, null=True)),
                ('secure_card_id', models.CharField(blank=True, max_length=255, null=True)),
                ('rejection_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('refundable', models.BooleanField(default=False)),
                ('refund_status', models.CharField(blank=True, max_length=50, null=True)),
                ('refund_id', models.CharField(blank=True, max_length=255, null=True)),
                ('refund_amount', models.FloatField(blank=True, null=True)),
                ('refund_requested_amount', models.FloatField(blank=True, null=True)),
                ('refund_reject_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('refund_date', models.DateTimeField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('product_code', models.CharField(blank=True, max_length=255, null=True)),
                ('package_code', models.CharField(blank=True, max_length=255, null=True)),
                ('product_quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('sum_price', models.FloatField(blank=True, null=True)),
                ('vat', models.FloatField(blank=True, null=True)),
                ('vat_percent', models.FloatField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='subscription.subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
