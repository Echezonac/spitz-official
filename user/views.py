from multiprocessing import context
from django.shortcuts import render


# Create your views here.
def signup(request):
    context = {}
    
    return render(request, 'user/signup.html', context)


def login(request):
    context ={}
    
    return render(request, 'user/login.html', context)