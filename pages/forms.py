from dataclasses import fields
from tabnanny import verbose
from django import forms
from .models import *
from django.forms import ModelForm

# class UserSignupForm(forms.Form):

#     User_name = forms.CharField(max_length=255 , label='Username' )
#     Password = forms.CharField(max_length=50 , widget=forms.PasswordInput , label= 'Password' )
#     Confirm_Password = forms.CharField(max_length=50 , widget=forms.PasswordInput , label='Confirm Password' )
#     Email = forms.EmailField(max_length=255 , label='Email')

#     def __str__(self): 
#         return self.User_name

class User_Sign_new(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'


class User_SignIn_new(forms.ModelForm):
    class Meta:
        model = SignIn
        fields = '__all__'
