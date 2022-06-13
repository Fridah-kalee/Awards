from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    project=Project.all_projects()
    my_projects = []
    for project in project:
        pic = Profile.objects.filter(user=project.user).first()
        if pic:
            pic = pic.image.url
        else:
            pic = ''
        obj = dict(
            title=project.title,
            image=project.image,
            avatar=pic,
            description=project.description,
            author=project.user,
            date_created=project.date_created,
        )
        my_projects.append(obj)

    return render(request, 'home.html',{"my_projects":my_projects})


@login_required(login_url='/accounts/login/')
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'django_registration/registration_form.html', {'form': form})    

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f'Your account has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }

    return render(request, 'update_profile.html', context)    

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
           
            image.save()
            
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def review(request, post):
    post = Project.objects.get(title=post)
    ratings = Ratings.objects.filter(user=request.user, post=post).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            post_ratings = Ratings.objects.filter(post=post)
            design_ratings = [des.design_rate for des in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)
            usability_ratings = [usa.usability_rate for usa in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)
            content_ratings = [content.content_rate for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)
            overall_score = (design_average + usability_average + content_average) / 3
            print(overall_score)
            rate.design_average = round(design_avr, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.overall_score = round(overall_score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'post': post,
        'rating_form': form,
        'rating_status': rating_status
    }
    return render(request, 'ratings.html', params)        