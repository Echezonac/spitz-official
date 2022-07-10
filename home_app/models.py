from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class Spit(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000,blank=True)
    time = models.TimeField(auto_now=True)
    images = models.ImageField(blank=True)
    
    def __str__(self):
        return self.author + ' ' + self.time
    
class SpitImage(models.Model):
    spitz = models.ForeignKey(Spit, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/')
    
    def __str__(self):
        return self.spitz.author + ' ' + self.spitz.time

    

    