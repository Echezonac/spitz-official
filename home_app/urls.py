import imp
from django.urls import path
from .views import DetailPostView, HomeView,profile,notification,settings,DetailPostView,CreatePostView,UpdatePostView,DeletePostView,CategoryView


urlpatterns = [
    path('home/', HomeView.as_view() ,name='home_page'),
    path('spitz/<int:pk>/', DetailPostView.as_view() , name='post-detail'),
    path('home/new/', CreatePostView.as_view(), name='new_post'),
    path('spitz/<int:pk>/delete/',DeletePostView.as_view(), name ='post_delete'),
    path('spitz/<int:pk>/edit/',UpdatePostView.as_view(), name ='post_edit'),
    path('category/<str:cats>/', CategoryView, name="cats_page"),
    path('profile/',profile,name="profile-page"),
    path('notify/',notification,name="notify-page"),
    path('settings/',settings, name='setting-page')
] 