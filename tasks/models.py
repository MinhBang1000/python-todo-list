from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    checked = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)