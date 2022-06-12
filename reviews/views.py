from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import UserUpdateForm, SignUpForm, NewProjectForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    project=Project.all_projects()
    my_projects= []
    for project in project:

        pic=Profile.objects.filter(user=project.user).first()
        if pic:
           pic=pic.profile_pic.url
        else:
            pic=''
        obj = dict(
            title=project.title,
            image=project.image,
            link=project.link,
            description=project.description,
            avatar=pic,
            date_created=project.date_created,
            author=project.user
        )
        my_projects.append(obj)   


    return render(request,'home.html',{'my_projects':my_projects})

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