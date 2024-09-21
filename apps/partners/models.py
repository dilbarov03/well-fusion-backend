import random
import string

from django.db import models

from apps.common.models import BaseModel


class Gym(BaseModel):
    name = models.CharField(max_length=255)
    promo_code = models.CharField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gym"
        verbose_name_plural = "Gyms"
        db_table = "gym"

    def generate_promo_code(self):
        """Generate a promo code based on the gym's name."""
        # Use the first 3 characters of the gym's name, convert to uppercase
        base_code = self.name[:3].upper()

        # Generate a random string of 5 alphanumeric characters
        characters = string.ascii_uppercase + string.digits
        random_part = ''.join(random.choice(characters) for _ in range(3))

        promo_code = f"{base_code}-{random_part}"

        while Gym.objects.filter(promo_code=promo_code).exists():
            random_part = ''.join(random.choice(characters) for _ in range(3))
            promo_code = f"{base_code}-{random_part}"

        return promo_code

    def save(self, *args, **kwargs):
        if not self.promo_code:
            self.promo_code = self.generate_promo_code()
        super().save(*args, **kwargs)