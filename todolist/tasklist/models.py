from django.db import models
from colorfield.fields import ColorField
from datetime import datetime

# Create your models here.

class Task(models.Model):
    given = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(null=True)
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)
    category = ColorField(default=[255, 0, 0])
