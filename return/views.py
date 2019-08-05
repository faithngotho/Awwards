from django.shortcuts import render,redirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 
