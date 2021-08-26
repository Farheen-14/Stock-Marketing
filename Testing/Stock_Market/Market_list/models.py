from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class stock_items(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  #adding for unique values 
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    video_url = models.URLField(max_length=300) #we can put here video urls
    # video = models.FileField(upload_to='media' ,null=True, blank=True) we can use also for adding video from our folder

class enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=200)