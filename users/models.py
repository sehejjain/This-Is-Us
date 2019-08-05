from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.conf import settings
from phone_field import PhoneField
from django.contrib.auth.decorators import login_required, user_passes_test


class User(AbstractUser):
    isUser = models.BooleanField(default=False)
    isOrg = models.BooleanField(default=False)

    def is_org(self):
        if str(self.isOrg) == True:
            return True
        else:
            return False
    org_login_required = user_passes_test(lambda u: True if u.is_org else False, login_url='/')

    def org_login_required(view_func):
        decorated_view_func = login_required(org_login_required(view_func), login_url='/')
        return decorated_view_func

    def __str__(self):
        return self.username

class OrgProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orgprofile')
    image = models.ImageField(default ='default.png', upload_to='profile_pics')
    complete = models.BooleanField(default=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')#add international phone number field
    name = models.CharField(max_length = 200, blank = True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userprofile')
    image= models.ImageField(default ='default.png', upload_to='profile_pics')
    complete = models.BooleanField(default=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')#add international phone number field
    name = models.CharField(max_length = 200, blank = True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
