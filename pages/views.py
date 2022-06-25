from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def index(request):
    return render(request ,'pages/index.html')


def about(request):
    return render(request ,'pages/about.html')



@csrf_exempt
def singup(request):
    if request.method == 'POST':
        dataform = User_Sign_new(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request ,'pages/singup.html',{'form': User_Sign_new})
    



def singin(request):
    # if request.POST.get('submit')=='sign_up':            
    #     User_name=request.POST.get('User_name')
    #     Password=request.POST.get('Password')

    if request.method == 'POST':
        dataformIn = User_SignIn_new(request.POST)
        if dataformIn.is_valid():
            dataformIn.save()
    return render(request ,'pages/singin.html',{'formIn': User_SignIn_new})



def p_1(request):
    return render(request ,'pages/p_1.html')







