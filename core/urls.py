from django.urls import path, include
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('org/create', views.create_volloc, name = 'createLoc')

]
