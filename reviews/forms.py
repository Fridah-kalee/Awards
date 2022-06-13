from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['bio']


class  NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','url','description',]

class RatingsForm(forms.ModelForm):

    class Meta:
        model = Ratings
        fields= ['design_rate','usability_rate','content_rate','overall_score']     