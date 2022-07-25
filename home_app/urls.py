from django.urls import path
from home_app import views

urlpatterns = [
    path('', views.home,name='home_page'),
    path('spitz/',views.detail_spitz, name='spitz-detail'),
    path('profile/',views.profile,name="profile-page"),
    path('notify/',views.notification,name="notify-page"),
    path('review/',views.review, name='review-page'),
    path('settings/',views.settings, name='setting-page')
] 