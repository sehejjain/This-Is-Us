from django.urls import path, include
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [

    path('register/org', views.registerOrg, name='registerOrg'),
    path('logout', views.orgLogout, name='logout'),
    path('register/user', views.registerUser, name='registerUser'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register_redirect'),
    path('login', LoginView.as_view(template_name = 'users/login.html', authentication_form=LoginForm), name = 'login'),


]
