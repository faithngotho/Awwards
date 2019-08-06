from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm,AddProjectForm,UserUpdateForm,proForm
from . models import Projects,Profile
from django.http import HttpResponse, Http404,HttpResponseRedirect
# Create your views here.


def home(request):
    projects=Projects.get_projects()
    return render(request, 'home.html',{"projects":projects})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 
@login_required(login_url='/accounts/login/')
def search_project(request):
    
    if 'projects' in request.GET and request.GET["projects"]:
        repos = request.GET.get("projects")
        searched_projects = Project.search_project(repos)
        print(searched_projects)
        message = f"{repos}"

        return render(request, 'search.html', {"message": message, "project": searched_projects})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html', {"message": message})
@login_required(login_url='/accounts/login/')
def add_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')

    else:
        form = AddProjectForm()
    return render(request, 'new_project.html',{"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    id = current_user.id
    project = Project.filter_by_user_id(id)
    return render(request, "profile/profile.html", {"project":project})

@login_required(login_url='/accounts/login/')
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance = request.user)
    return render(request, "profile/user-up.html",{"form":form})

@login_required(login_url='/accounts/login/')
def myprofile(request):
    current_user = request.user
    if request.method =='POST':
        form = proForm(request.POST,request.FILES)
        if form.is_valid():
            myprofile=form.save(commit=False)
            myprofile.username =current_user
            myprofile.save()
            return redirect('profile')
    else:
        form=proForm()
    return render(request, 'profile/profile-up.html',{"form":form})
