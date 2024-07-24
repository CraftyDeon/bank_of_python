from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm1, UserForm2

def index(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserForm1(request.POST)
        profile_form = UserForm2(request.POST)
        if form.is_valid() and profile_form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['pass1']
            new_user = User.objects.create_user(username=username, password=password)
            dob = profile_form.cleaned_data['dob']
            age = profile_form.cleaned_data['age']
            gender = profile_form.cleaned_data['gender']
            phno = profile_form.cleaned_data['phno']
            gmail = profile_form.cleaned_data['gmail']
            address = profile_form.cleaned_data['address']
            profile = UserProfile.objects.create(user=new_user, dob=dob, age=age, gender=gender,
                                                  phno=phno, gmail=gmail, address=address)
            return redirect('/')
    else:
        form = UserForm1()
        profile_form = UserForm2()
    return render(request, 'register.html', {'form': form, 'profile_form': profile_form})

def loogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def loogout(request):
    logout(request)
    return redirect('/')
