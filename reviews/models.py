from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=30)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile/',blank=True,default='')
    date_created =models.DateField(auto_now_add=True)
    
    def save_profile(self):
        self.save
    
    def __str__(self):
        return self.username 

class Project(models.Model):
    title = models.TextField(max_length=30)
    link= models.URLField(max_length=200)
    description = models.TextField(max_length=300)
    date_created= models.DateField(auto_now_add=True )

    def save_project(self):
        self.save()

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects    
