from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    text = models.TextField()

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        db_table = "message"

    def __str__(self):
        return self.full_name
