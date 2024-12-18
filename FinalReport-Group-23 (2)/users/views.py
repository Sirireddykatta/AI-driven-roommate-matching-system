from django.shortcuts import render,redirect
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login,logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse




# Create your views here.
@login_required
def index(request):
    logged_in_user = request.user
    return render(request,'users/index.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a home page or wherever you like
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'users/login.html')



def signup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserProfileForm()
    
    return render(request, 'users/signup.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to login page after logging out

@login_required
def profile(request):
    logged_in_user = request.user

    return render(request,'users/profile.html')