""" IMPORTs"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from project.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
