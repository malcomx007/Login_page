from django import views
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('profile/', views.profile , name='profile'),

]


