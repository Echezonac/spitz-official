from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    content = models.TextField()
    # time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.nickname + ' - ' + self.content

    def get_absolute_url(self): # new
        return reverse('home_page')
