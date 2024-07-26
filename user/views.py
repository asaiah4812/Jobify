from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import RegisterUserForm
from resume.models import Resume
from company.models import Company


# Create your views here.
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created. please login to continue')
            return redirect('user:login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('user:register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'user/register_applicant.html', context)
    

def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created. please login to continue')
            return redirect('user:login')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('user:register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'user/register_recruiter.html', context)
    
    
# login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, f'Hi {username} Welcome to Jobify Dashboard')
            return redirect('dashboard:dashboard')
        else:
            messages.warning(request, 'something went wrong')
            return redirect('user:login')
    else:
        return render(request, 'user/login.html')
    

def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended. Login to start a new session')
    return redirect('user:login')