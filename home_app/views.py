from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm,EditForm



class HomeView(ListView):
    model = Post
    template_name = 'pages/index.html'
    ordering = ['-post_date']


class DetailPostView(DetailView):
    model = Post
    template_name = 'pages/spitz-detail.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/create_post.html'
    # fields = ["body","author","category"]

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'pages/update_post.html'
    # fields = ['body','category']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'pages/delete_post.html'
    success_url = reverse_lazy('home_page')

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
