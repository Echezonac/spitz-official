from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )
    body = models.TextField()

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})



    

    