from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    prof_pic=models.ImageField(upload_to='pictures/',default='default.png')
    name=models.CharField(max_length=50)
    bio=models.TextField()
    location=models.CharField(max_length=100)
    account_url=models.URLField()

