import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Task(models.Model):

    id = models.UUIDField(blank=False, null=False, primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(default=3600)
    options = models.TextField(default='{}', null=False)