# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.db import models
from myHospital.models import Patient,Doctor,Reviewals,Test,Prescription,Diagnosis,HealthFacility,Nurse,Registrar,LabTechnician
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        #YOUR CODE HERE
       form=LoginForm(request.POST)
       uname = request.POST['username'
]   # user's username is kept in a dictionary
       passwd = request.POST['password']  # user's password is kept in a dictionary
       
       
       user = authenticate(username=uname, password=passwd)
       
       if user is not None :
       	   if user.is_active:
             login(request,user)
             current_user = request.user	
             if Doctor.objects.filter(user = current_user):
               return HttpResponseRedirect("/doctor_page")
             elif Patient.objects.filter(user = current_user):
               return HttpResponseRedirect("/patient_page")
             elif Nurse.objects.filter(user = current_user):
               return HttpResponseRedirect("/nurse_page")
             elif Registrar.objects.filter(user = current_user):
               return HttpResponseRedirect("/registrar_page")
             elif LabTechnician.objects.filter(user = current_user):
               return HttpResponseRedirect("/labtec_page")
           else:
               return HttpResponse('invalid username and password!!!')   
           
       else:
            return HttpResponse("wrong Username or password. User Authentication failed!!!")
       
           
  

    form = LoginForm()
    return render_to_response('healthprovider/login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('healthprovider/logout.html')

def home(request):
     return render_to_response('Hospital/base.html',{})


# Create your views here.
