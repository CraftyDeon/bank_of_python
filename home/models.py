from django.db import models
from django.contrib.auth.models import User
class user(models.Model):
    username = models.TextField(max_length=100)
    pass1 = models.CharField(max_length=100)
    pass2 = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phno = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


    def __str__(self):
        return self.user.username