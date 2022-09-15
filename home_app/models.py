from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, time

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )
    body = models.TextField()
    category =  models.CharField(max_length=100, default='Event')
    post_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})



    

    