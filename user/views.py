from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                messages.error(request, "Username or email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                auth.login(request, user)
                messages.success(request, "You have registered successfully")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
    context = {}
    
    return render(request, 'user/signup.html', context)


def logout(request):
    auth.logout(request)
    
    return redirect('login')