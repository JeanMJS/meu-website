from django.contrib import admin
from django.urls import include, path

from project.views import home

urlpatterns = [
    path('', home),
]
