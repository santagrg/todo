from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("addemp/", employee, name="employee"),
    path("delete/<int:roll>/", edelete),
    path("edit/<int:roll>/", edit_emp)
]