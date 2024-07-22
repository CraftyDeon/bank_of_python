from django.contrib import admin
from .models import user,UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(user)