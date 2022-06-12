from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=30)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile/',blank='True',default='default.png')
    user =models.OneToOneField(User, on_delete = models.CASCADE,null='True')
    date_created =models.DateField(auto_now_add=True)

    
    
    def save_profile(self):
        self.save
    
    def __str__(self):
        return f'{self.user.username} Profile' 

class Project(models.Model):
    title = models.TextField(max_length=30)
    image =models.ImageField(upload_to ='home/',blank=True)
    link= models.URLField(max_length=200)
    description = models.TextField(max_length=300)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default='',null=True,related_name='author')
    date_created= models.DateField(auto_now_add=True )

    def save_project(self):
        self.save()

    @classmethod
    def all_projects(cls):
        projects =cls.objects.all()
        return projects 

    @property
    def image_url(self):
      if self.image and hasattr(self.image, 'url'):
        return self.image.url       

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects    
