from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('home')
