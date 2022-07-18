from django.shortcuts import render
from .models import *


def home(request):
    context = {}
    return render(request,'pages/index.html',context)

def detail_spitz(request):
    context = {}
    return render(request,'pages/spitz-detail.html',context)
    

