from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from .models import VolLoc
@receiver(post_save, sender = User)
def create_volloc(sender, instance, created,  **kwargs):
    if created:
        if instance.isUser:
            print("Invalid, User Cannot Create a Volunteering Location")
        else:
            VolLoc.objects.create(user=instance)
