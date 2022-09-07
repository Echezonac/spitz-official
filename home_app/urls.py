import imp
from django.urls import path
from .views import DetailPostView, HomeView,profile,notification,settings,review,DetailPostView,CreatePostView,UpdatePostView,DeletePostView


urlpatterns = [
    path('home/', HomeView.as_view() ,name='home_page'),
    path('spitz/<int:pk>/', DetailPostView.as_view() , name='post-detail'),
    path('home/new/', CreatePostView.as_view(), name='new_post'),
    path('spitz/<int:pk>/delete/',DeletePostView.as_view(), name ='post_delete'),
    path('spitz/<int:pk>/edit/',UpdatePostView.as_view(), name ='post_edit'),
    path('profile/',profile,name="profile-page"),
    path('notify/',notification,name="notify-page"),
    path('review/',review, name='review-page'),
    path('settings/',settings, name='setting-page')
] 