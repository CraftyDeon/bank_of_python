from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('form/',views.login,name='form'),
]