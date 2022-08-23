from django.shortcuts import render
from .models import *


def home(request):

    context = {
        'page_name': 'Home',  # Name of the current page,
    }
    return render(request, 'pages/index.html', context)


def detail_spitz(request):
    context = {
        'page_name': 'Spitz',  # Name of the current page,
    }
    return render(request, 'pages/spitz-detail.html', context)


def profile(request):
    context = {
        'page_name': 'Profile',  # Name of the current page,
    }
    return render(request, 'pages/profile.html', context)


def notification(request):
    context = {
        'page_name': 'Notifications',  # Name of the current page,
    }
    return render(request, 'pages/notify.html', context)


def settings(request):
    context = {
        'page_name': 'Settings',  # Name of the current page
    }
    return render(request, 'pages/settings.html', context)
