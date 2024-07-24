from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.loogin,name='login'),
    path('logout/',views.loogout,name='logout'),
]