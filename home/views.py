from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm1, UserForm2

def index(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        profile_form = UserForm2(request.POST)
        if  profile_form.is_valid():
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

    return render(request, 'register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        form = UserForm1(request.POST)
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['pass1']
            profile = User.objects.create_user(username=username, password=password)
            return redirect('/')
    else:
        profile = UserForm2()
    return render(request, 'form.html',{'profile': profile})