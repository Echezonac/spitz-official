from django.urls import path
from .views import reviews

urlpatterns = [
    path('reviews/', reviews, name='reviews')
]