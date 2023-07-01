from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", signin, name="signin"),
    path("signup/", signup, name="signup"),
    path("home/", home, name="home"),
    path("logout/", logout_view, name="logout"),
]