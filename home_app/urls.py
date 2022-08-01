from django.urls import path
from home_app.views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home_page'),
    path('spitz/<int:pk>/',SpitDetailView.as_view(), name='spitz-detail'),
    path('addspit/',AddSpitView.as_view(), name='add-spit-page'),
    path('update-spitz/edit/<int:pk>/',UpdateSpitView.as_view(), name='update-spitz-page'),
    path('profile/',profile, name="profile-page"),
    path('notify/',notification, name="notify-page"),
    path('review/',review, name='review-page'),
    path('settings/',settings, name='setting-page')
] 