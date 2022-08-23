from django.shortcuts import render
from .models import *


def home(request):
    context = {}
    return render(request,'pages/index.html',context)

def detail_spitz(request):
    context = {}
    return render(request,'pages/spitz-detail.html',context)

def profile(request):
    context = {}
    return render(request,'pages/profile.html',context)


def notification(request):
    context = {}
    return render(request,'pages/notify.html',context)


def settings(request):
    context = {}
    return render(request,'pages/settings.html',context)

