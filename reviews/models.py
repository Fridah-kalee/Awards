from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=30)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile/',blank=True,default='')
    date_created =models.DateField(auto_now_add=True) 