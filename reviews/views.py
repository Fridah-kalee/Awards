from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Project
from django.contrib.auth import authenticate,login,logout

# Create your views here.
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

def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})