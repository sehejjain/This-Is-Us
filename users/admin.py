from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models import OrgProfile, UserProfile


class UserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username',]

admin.site.register(User, UserAdmin)


admin.site.register(OrgProfile)
admin.site.register(UserProfile)
