from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView

class HomeView(ListView):
    model = Post
    template_name = 'pages/index.html'
   

class SpitDetailView(DetailView):
    model = Post
    template_name = 'pages/spitz-detail.html'

class AddSpitView(CreateView):
    model = Post
    template_name = 'pages/add-spit.html'
    fields = '__all__'

class UpdateSpitView(UpdateView):
    model = Post
    template_name = 'pages/update-spit.html'
    fields = '__all__'

def profile(request):
    context = {}
    return render(request,'pages/profile.html',context)


def notification(request):
    context = {}
    return render(request,'pages/notify.html',context)
    
def review(request):
    context = {}
    return render(request,'pages/review.html',context)

def settings(request):
    context = {}
    return render(request,'pages/settings.html',context)

