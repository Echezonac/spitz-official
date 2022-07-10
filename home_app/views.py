from django.shortcuts import render,get_object_or_404
from .models import *


def home(request):
    spitz = Spit.objects.all()
    return render(request,'pages/index.html',{'spitz':spitz})

def spit_detail_view(request):
    spitz = get_object_or_404(Spit,id=id)
    photos = SpitImage.objects.filter(spitz=spitz)
    return render(request,'pages/spitz_detail.html',{'spitz':spitz,'photos':photos})