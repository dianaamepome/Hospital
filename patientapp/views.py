# Create your views here.
# Create your views here.

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from myHospital.models import Patient,Doctor,Reviewals,Test,Prescription,Diagnosis,HealthFacility

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        #YOUR CODE HERE
       uname = request.POST['username']   # user's username is kept in a dictionary
       passwd = request.POST['password']  # user's password is kept in a dictionary
       user = authenticate(username=uname, password=passwd)
       if user is not None and user.is_active:
       	   
    	   login(request, user)  # redirect user to a success page
    	   currentuser = request.user
    	   if Patient.objects.filter(user = currentuser).count() is 1:
               return HttpResponseRedirect(" ")
           elif Patient.objects.filter(manager =currentuser).count() is 1:
                return HttpResponseRedirect(" ")
           else:
                return HttpResponseRedirect ("invalid username and password")
       else:
           return HttpResponse("wrong Username or password. User Authentication failed!!!") 
        

           
              
  

    form = LoginForm()
    return render_to_response('patientapp/login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated()
    })

@csrf_exempt
def do_logout(request):
    logout(request)
    return render_to_response('patientapp/logout.html')

def home(request):
    return render_to_response('Hospital/base.html',{'user':request.user})
