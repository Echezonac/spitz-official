from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post,Category
from .forms import PostForm,EditForm



class HomeView(ListView):
    model = Post
    template_name = 'pages/index.html'
    ordering = ['-post_date']
    
    def get_context_data(self,*args,**kwargs):
        cat_option = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_option"] = cat_option
        return context
    
def CategoryView(request, cats,):
    category_post = Post.objects.filter(category = cats)
    cat_option = Category.objects.all()
    return render(request,'pages/category.html',{'cats':cats,'category_post':category_post,'cat_option':cat_option})
    
   



class DetailPostView(DetailView):
    model = Post
    template_name = 'pages/spitz-detail.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_option = Category.objects.all()
        context = super(DetailPostView, self).get_context_data(*args, **kwargs)
        context["cat_option"] = cat_option
        return context

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
