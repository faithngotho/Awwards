from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile') 


class Projects(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(default = 'default.jpg',upload_to='images/')
    description = models.CharField(max_length =200)
    link = models.URLField()
    ratings = models.IntegerField(blank=True, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE) 
