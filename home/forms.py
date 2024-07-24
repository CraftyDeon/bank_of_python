from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class UserForm1(forms.ModelForm):
    pass1 = forms.CharField(widget=forms.PasswordInput)
    pass2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserProfile
        fields = ['username', 'pass1', 'pass2','dob', 'age', 'gender', 'phno', 'gmail', 'address']
class UserForm2(forms.ModelForm):
    pass1 = forms.CharField(widget=forms.PasswordInput)
    pass2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'pass1', 'pass2']
