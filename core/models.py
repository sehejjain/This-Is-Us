from django.db import models
from users.models import User
from django.contrib.auth.models import (
    AbstractUser, BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone

from django.db.models.signals import post_save
from django.conf import settings
from location_picker.fields import LocationField


# A Volunteering Location
class VolLoc(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name="loc")
    name = models.CharField(max_length = 100)
    location = LocationField(
        max_length=256,
        null=True,
        blank=True
    )
    contact_email = models.EmailField()
    contact_phone = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
