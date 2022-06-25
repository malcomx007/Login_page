import email
from secrets import choice
from django import forms
from django.db import models
from django.forms import PasswordInput, Widget

# Create your models here.

class SignUp(models.Model):

    User_name = models.CharField(max_length=255 , null=False , verbose_name= 'Username')
    Password = models.CharField(max_length=50 , null=False , verbose_name= 'Password' )
    Confirm_Password = models.CharField(max_length=50 , null=False , verbose_name='Confirm Password')
    Email = models.EmailField(max_length=255 , null=False ,verbose_name='Email')


    def __str__(self): 
        return self.User_name


class SignIn(models.Model):

    User_name = models.CharField(max_length=255 , null=False , verbose_name= 'Username')
    Password = models.CharField(max_length=50 , null=False , verbose_name= 'Password' )


    def __str__(self): 
        return self.User_name

