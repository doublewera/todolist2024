from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE, null=True, blank=True, default=None)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.CASCADE, null=True, blank=True, default=None)
    given = models.DateTimeField(default=datetime.now)
    softline = models.DateTimeField(null=True, blank=True, default=None)
    deadline = models.DateTimeField(null=True)
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)
    #category = models.CharField(default="#ff0000")#ColorField(default="#ff0000")
