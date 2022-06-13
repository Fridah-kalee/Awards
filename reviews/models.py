from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=30)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile/',blank='True',default='default.png')
    user =models.OneToOneField(User, on_delete = models.CASCADE,null='True')
    date_created =models.DateField(auto_now_add=True)

    
    
    def save_profile(self):
        self.save

    def delete_user(self):
        self.delete()    
    
    def __str__(self):
        return f'{self.user.username} Profile' 

class Project(models.Model):
    title = models.TextField(max_length=30)
    image =models.ImageField(upload_to ='home/',default ='my image')
    url= models.URLField(max_length=200)
    description = models.TextField(max_length=300)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default='',null=True,related_name='author')
    date_created= models.DateField(auto_now_add=True )

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()    

    @classmethod
    def all_projects(cls):
        projects =cls.objects.all()
        return projects 
       

    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects 

class Ratings(models.Model):
    ratings=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10',)
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    design_rate = models.IntegerField(choices=ratings, default=0, blank=True)
    usability_rate = models.IntegerField(choices=ratings, blank=True, default=0)
    content_rate = models.IntegerField(choices=ratings, blank=True,default=0)
    overall_score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    
    def save_ratings(self):
        self.save()
    
    def __str__(self):
        return f'{self.post} Ratings'
    
    @classmethod
    def get_ratings(cls, id):
        ratings = Ratings.objects.filter(project_id=id).all()
        return ratings           
