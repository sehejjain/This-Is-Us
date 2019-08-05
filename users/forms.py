from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm

from django.db import transaction
from .models import User
from .models import OrgProfile, UserProfile


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class UserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
            ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.isUser = True
        user.isOrg=False
        user.save()
        userprofile = UserProfile.objects.create(user=user)
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password'

    def clean(self):    
        cleaned_data = super(UserSignUpForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                print("error")
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

class OrgSignUpForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
            ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.isOrg = True
        user.isUser=False
        user.save()
        orgprofile = OrgProfile.objects.create(user=user)
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = '__all__'



class OrgProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = OrgProfile
        exclude = [
        'user',
        'complete',
        'image',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = [
        'complete',
        'image',
        'user'
        ]
