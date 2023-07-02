from django.contrib import admin
from django.urls import path, include
from .views import *

app_name="crud"
urlpatterns = [
    path("addemp/", employee, name="employee"),
    path("delete/<int:roll>/", edelete, name="delete"),
    path("edit/<int:roll>/", edit_emp, name="edit"),
    path("doedit/<int:roll>/", do_edit_emp, name="doedit")
]