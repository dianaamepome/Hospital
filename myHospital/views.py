from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render_to_response
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from myHospital.models import Patient,Doctor,Reviewals,Test,Prescription,Diagnosis,HealthFacility,Report,Comment,Vitals,Nurse,Registrar,LabTechnician
from django.core import serializers



def home(request):
    return render_to_response('Hospital/base.html',{'user':request.user})
 

def back_to_homepage(request):
    return render_to_response('Hospital/homepage.html') 


def frontpage(request):  
    return render_to_response ('Hospital/homepage.html')


def contact_us(request):
    return render_to_response('Hospital/contact_us.html')


def about_us(request):
    return render_to_response('Hospital/about_us.html')

     
@csrf_exempt
def patient_page(request):
    current_user = request.user
    pat= Patient.objects.get(user = current_user)
    return render_to_response('Hospital/patient_page.html',{'user':request.user,'pat':pat})

@csrf_exempt
def nurse_pagebase(request):
    current_user = request.user
    nurse= Nurse.objects.get(user = current_user)
    return render_to_response('Hospital/nurse_pagebase.html',{'user':request.user,'nurse':nurse})



@csrf_exempt
def nurse_page(request):
    current_user = request.user
    nurse= Nurse.objects.get(user = current_user)
    return render_to_response('Hospital/nurse_page.html',{'user':request.user,'nurse':nurse})

@csrf_exempt
def labtec_page(request):
    current_user = request.user
    labtec= LabTechnician.objects.get(user = current_user)
    return render_to_response('Hospital/labtec_page.html',{'user':request.user,'labtec':labtec})

       

def faq(request):
    return render_to_response('hostels/faq.html', {})


@csrf_exempt
@login_required
def doctor_page(request):
    current_user = request.user
    doc= Doctor.objects.get(user = current_user)   
    return render_to_response('Hospital/doctor_page.html',{'user':request.user})

@csrf_exempt
@login_required
def registrar_page(request):
    current_user = request.user
    registrar= Registrar.objects.get(user = current_user)   
    return render_to_response('Hospital/registrar_page.html',{'user':request.user})



class RegistrationForm(ModelForm):
      username = forms.CharField(max_length=20)
      password = forms.CharField(widget=forms.PasswordInput())
      confirm_password = forms.CharField(widget=forms.PasswordInput()) 
      date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), initial = "DD-MM-YYYY")
      class Meta:
         
         model=Doctor
         widgets = {'password':forms.PasswordInput(),}
         exclude =('user',) 




@csrf_exempt
def doctorreg(request):
    if request.method == 'POST':
	user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
	doctor = Doctor(user=user)
      	print "User submitted data"
	form = 	RegistrationForm(request.POST, request.FILES, instance=doctor)
	print request.POST["username"], request.POST["email"], request.POST["password"]
        
        if form.is_valid():
	    
            print "It validated"
            form.save()
	    user = authenticate(username=request.POST["username"], password=request.POST["password"])
	    login(request, user)
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        form = 	RegistrationForm()
    return render_to_response('Hospital/doctor_registrationpage.html',{'form':form,'user':request.user})



class RegistrarForm(ModelForm):
      username = forms.CharField(max_length=20)
      password = forms.CharField(widget=forms.PasswordInput())
      confirm_password = forms.CharField(widget=forms.PasswordInput()) 
      date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), initial = "DD-MM-YYYY")
      class Meta:
         
         model=Registrar
         widgets = {'password':forms.PasswordInput(),}

         exclude =('user',) 




@csrf_exempt
def Registrarreg(request):
    if request.method == 'POST':
	user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
	registrar = Registrar(user=user)
      	print "User submitted data"
	form = 	RegistrarForm(request.POST, request.FILES, instance=registrar) 
	print request.POST["username"], request.POST["email"], request.POST["password"]
        
        if form.is_valid():
	    
            print "It validated"
            form.save()
	    user = authenticate(username=request.POST["username"], password=request.POST["password"])
	    login(request, user)
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        form = 	RegistrarForm()
    return render_to_response('Hospital/registrar_registrationpage.html',{'form':form,'user':request.user})





class Patient_RegistrationForm(ModelForm):
      username = forms.CharField(max_length=20)
      password = forms.CharField(widget=forms.PasswordInput())
      confirm_password = forms.CharField(widget=forms.PasswordInput()) 
      date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), initial = "DD-MM-YYYY")
      class Meta:
         
         model=Patient
         widgets = {'password':forms.PasswordInput(),}
         exclude =('user','doctor')
 

@csrf_exempt
def patientreg(request):
    if request.method == 'POST':
	user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
	patient = Patient(user=user)
      	print "User submitted data"
	myform = Patient_RegistrationForm(request.POST, request.FILES, instance=patient) 
        if myform.is_valid():    
            print "It validated"
            myform.save()
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        myform =Patient_RegistrationForm()
    return render_to_response('Hospital/patient_registrationpage.html',{'form':myform,'user':request.user})


class nurse_RegistrationForm(ModelForm):
      username = forms.CharField(max_length=20)
      password = forms.CharField(widget=forms.PasswordInput())
      confirm_password = forms.CharField(widget=forms.PasswordInput()) 
      date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), initial = "DD-MM-YYYY")
      class Meta:
         
         model=Nurse
         widgets = {'password':forms.PasswordInput(),}
         exclude =('user',)
 

@csrf_exempt
def nursereg(request):
    if request.method == 'POST':
	user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
	nurse = Nurse(user=user)
      	print "User submitted data"
	myform = nurse_RegistrationForm(request.POST, request.FILES, instance=nurse) 
        if myform.is_valid():    
            print "It validated"
            myform.save()
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        myform =nurse_RegistrationForm()
    return render_to_response('Hospital/nurse_registrationpage.html',{'form':myform,'user':request.user})


class Labtec_RegistrationForm(ModelForm):
      username = forms.CharField(max_length=20)
      password = forms.CharField(widget=forms.PasswordInput())
      confirm_password = forms.CharField(widget=forms.PasswordInput()) 
      date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), initial = "DD-MM-YYYY")
      class Meta:
         
         model=LabTechnician
         widgets = {'password':forms.PasswordInput(),}
         exclude =('user',)
 

@csrf_exempt
def LabTechnicianreg(request):
    if request.method == 'POST':
	user = User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
	labtec = LabTechnician(user=user)
      	print "User submitted data"
	myform = Labtec_RegistrationForm(request.POST, request.FILES, instance=labtec) 
        if myform.is_valid():    
            print "It validated"
            myform.save()
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        myform =Labtec_RegistrationForm()
    return render_to_response('Hospital/Lab_registrationpage.html',{'form':myform,'user':request.user})







@csrf_exempt
@login_required
def edit_patientreg(request,id):
   current_user = request.user
   register= Registrar.objects.get(user = current_user)
   q=Patient.objects.get(ODP_number=id)
   if request.method == 'POST':
    
       form = Patient_RegistrationForm(request.POST, request.FILES ,instance=q) 
       if form.is_valid():
           form.save()
           user = authenticate(username=request.POST["username"], password=request.POST["password"])
	   login(request, user)
           return HttpResponseRedirect('')
   else:
       form = Patient_RegistrationForm(instance=q)
       my_context = Context({'patientregedit':q,'form':form,'user':request.user})
       return render_to_response ('Hospital/edit_patientreg.html',my_context)

@csrf_exempt
@login_required
def patient_list(request):
    patient_list = Patient.objects.all()
    t = loader.get_template("Hospital/patient_list.html")
    c = Context({ 'patient_list': patient_list ,'user':request.user})
    return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def reg_pat_admin(request):
    patient_list = Patient.objects.all()
    t = loader.get_template("Hospital/reg_pat_admin.html")
    c = Context({ 'patient_list': patient_list ,'user':request.user})
    return HttpResponse(t.render(c))



@csrf_exempt
def healthfacility_list(request):
    healthfacility_list = HealthFacility.objects.all()
    t = loader.get_template("Hospital/Reg_Healthfacilities.html")
    c = Context({ 'healthfacility_list':healthfacility_list })
    return HttpResponse(t.render(c))


@csrf_exempt
@login_required
def doctor_list(request):
    doctor_list = Doctor.objects.all()
    t = loader.get_template("Hospital/doctor_list.html")
    c = Context({ 'doctor_list':doctor_list ,'user':request.user})
    return HttpResponse(t.render(c))



def healthfacilitylist_search(request, term=True):
     if request.GET.get('q','')!='':
	 term=request.GET.get('q','')
     p=HealthFacility.objects.filter(HealthFacility_ID__contains=term)|HealthFacility.objects.filter(HealthFacility_name__contains=term)|  HealthFacility.objects.filter(city__contains=term)|HealthFacility.objects.filter(country__contains=term)|HealthFacility.objects.filter(email__contains=term)
         
     my_context = Context({ 'healthfacility_list':p,'term':term})
     return render_to_response ('healthfacilitylist_search.html', my_context)

@login_required
def patientlist_search(request, term=True):
     if request.GET.get('q','')!='':
	 term=request.GET.get('q','')
     p=Patient.objects.filter(ODP_number__contains=term)|Patient.objects.filter(first_name__contains=term)|  Patient.objects.filter(last_name__contains=term)|Patient.objects.filter(gender__contains=term)
         
     my_context = Context({'patient_list':p,'term':term,'user':request.user})
     return render_to_response ('Hospital/patient_list_search.html', my_context)
     
@csrf_exempt
@login_required
def prescriptionlist_search(request, term=True):
     if request.GET.get('q','')!='':
	 term=request.GET.get('q','')
     p=Prescription.objects.filter(id__contains=term)|Prescription.objects.filter(Prescription_Details__contains=term)|  Prescription.objects.filter(Prescription_date__contains=term)|Prescription.objects.filter(Medicine_Name__contains=term)|Prescription.objects.filter(Medicine_Doseage__contains=term)       
     my_context = Context({'prescription_list':p,'term':term,'user':request.user})

     return render_to_response ('Hospital/prescription_list_search.html', my_context)

@csrf_exempt
@login_required
def lablist_search(request, term=True):
     if request.GET.get('q','')!='':
	 term=request.GET.get('q','')
     p=Test.objects.filter(id__contains=term)|Test.objects.filter(Test_Name__contains=term)|  Test.objects.filter(Test_Result__contains=term)|Test.objects.filter(Test_date__contains=term)      
     my_context = Context({'lab_list':p,'term':term,'user':request.user})
     return render_to_response ('Hospital/lab_list_search.html', my_context)

@login_required
@csrf_exempt
def lab_list(request):
    lab_list = Test.objects.all()
    diagnosis_list = Diagnosis.objects.all()
    doctor_list = Doctor.objects.all()
    patient_list = Patient.objects.all()
    t = loader.get_template("Hospital/labtest.html")
    c = Context({ 'lab_list': lab_list, 'diagnosis_list': diagnosis_list,'patient_list': patient_list,'doctor_list': doctor_list,'user':request.user})
    return HttpResponse(t.render(c))


@csrf_exempt
@login_required
def diagnosis_list(request):
    diagnosis_list = Diagnosis.objects.all()
    doctor_list = Doctor.objects.all()
    patient_list = Patient.objects.all()
    t = loader.get_template("Hospital/diagnosis_list.html")
    c = Context({ 'diagnosis_list': diagnosis_list,'patient_list': patient_list,'doctor_list': doctor_list,'user':request.user})
    return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def prescription_list(request):
    prescription_list = Prescription.objects.all()
    patient_list = Patient.objects.all()
    doctor_list = Doctor.objects.all()
    t = loader.get_template("Hospital/prescription.html")
    c = Context({ 'prescription_list': prescription_list,'user':request.user,'doctor_list': doctor_list,'patient_list': patient_list})
    return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def diagnosislist_search(request, term=True):
     if request.GET.get('q','')!='':
	 term=request.GET.get('q','')
     p=Diagnosis.objects.filter(Diagnosis_ID__contains=term)|Diagnosis.objects.filter(Diagnosis_Majorcomplaints__contains=term)|  Diagnosis.objects.filter(Diagnosis_Details__contains=term)|Diagnosis.objects.filter(Diagnosis_date__contains=term)   
     my_context = Context({'diagnosis_list':p,'term':term,'user':request.user})
     return render_to_response ('Hospital/diagnosis_list_search.html', my_context)

@login_required
@csrf_exempt
def reviewal_list(request):
    reviewal_list = Reviewals.objects.all()
    patient_list = Patient.objects.all()
    doctor_list = Doctor.objects.all()
    t = loader.get_template("Hospital/Reviewal_list.html")
    c = Context({ 'reviewal_list': reviewal_list,'patient_list': patient_list,'doctor_list': doctor_list,'user':request.user})
    return HttpResponse(t.render(c))

@login_required
def reviewallist_search(request, term=True):
     if request.GET.get('q','')!='':
	 term=request.GET.get('q','')
     p=Reviewals.objects.filter(id__contains=term)|Reviewals.objects.filter(Reviewals_Date__contains=term)
     my_context = Context({'reviewal_list':p,'term':term,'user':request.user})
     return render_to_response ('Hospital/reviewal_list_search.html', my_context)

class Diagnosis_Form(ModelForm):
      class Meta:
         model=Diagnosis
         exclude=["doctor"]
         
         
@login_required         
@csrf_exempt
def diagnosis_details(request):
    current_user = request.user
    doc= Doctor.objects.get(user = current_user)
    thisdoc=Doctor.objects.get(user= current_user)
    status=False
    if request.method == 'POST':
        userinstance=Diagnosis(doctor=thisdoc)
      	print "User submitted data"
	theform = Diagnosis_Form(request.POST, request.FILES,instance=userinstance) 
        if theform.is_valid():
            print "It validated"
            theform.save()
            return HttpResponseRedirect('/prescription_details')
    else:
	print "It's not post"
        theform =Diagnosis_Form()
    return render_to_response('Hospital/add_diagnosis.html',{'form':theform,'user':request.user})


@csrf_exempt
@login_required
def edit_diagnosisdetails(request,id):
   q=Diagnosis.objects.get(pk=id)
   if request.method == 'POST':
    
       form = Diagnosis_Form(request.POST, instance=q)  
       if form.is_valid():
           user = request.user.id
           form.save()
       return HttpResponseRedirect(request.path)    
   else:
       form = Diagnosis_Form(instance=q)         
   my_context = Context({'diagnosisedit':q,'form':form,'user':request.user})
    
   return render_to_response ('Hospital/edit_diagnosisdetails.html',my_context)  


class Prescription_Form(ModelForm):
      class Meta:
         model=Prescription
         exclude=["doctor",'']
         
@csrf_exempt
@login_required
def prescription_details(request):
    current_user = request.user
    doc= Doctor.objects.get(user = current_user)
    thisdoc=Doctor.objects.get(user= current_user)
    status=False
    if request.method == 'POST':
        userinstance=Prescription(doctor=thisdoc)
      	print "User submitted data"
	itform = Prescription_Form(request.POST, request.FILES,instance=userinstance) 
        if itform.is_valid():
	    
            print "It validated"
            itform.save()
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        itform =Prescription_Form()
    return render_to_response('Hospital/prescription_page.html',{'form':itform,'user':request.user,'doc':doc})


@csrf_exempt
@login_required
def edit_prescriptiondetails(request,id):
   q=Prescription.objects.get(pk=id)
   if request.method == 'POST':
    
       form = Prescription_Form(request.POST, instance=q) 
       if form.is_valid():
           form.save()
       return HttpResponseRedirect(request.path)     
   else:
       form = Prescription_Form(instance=q)         

   my_context = Context({'Prescriptionedit':q,'form':form,'user':request.user})
    
   return render_to_response ('Hospital/edit_prescriptiondetails.html',my_context)  




class Reviewal_Form(ModelForm):
      Reviewals_Date = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), initial = "DD-MM-YYYY")
      Reviewals_Time = forms.TimeField(widget=forms.TimeInput(format = '%h:%m'), input_formats=('%h:%m',), initial = "h:m")
      class Meta:
         model=Reviewals
         exclude=["doctor"]


@csrf_exempt
@login_required
def reviewal_details(request):
    current_user = request.user
    doc= Doctor.objects.get(user = current_user)
    thisdoc=Doctor.objects.get(user= current_user)
    status=False
    if request.method == 'POST':
        userinstance=Reviewals(doctor=thisdoc)
      	print "User submitted data"
	revform = Reviewal_Form(request.POST, request.FILES,instance=userinstance) 
        if revform.is_valid():
	    
            print "It validated"
            revform.save()
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        revform =Reviewal_Form()
    return render_to_response('Hospital/reviewal_page.html',{'form':revform,'user':request.user,'doc':doc})

@csrf_exempt
@login_required
def edit_reviewaldetails(request,id):
   q=Reviewals.objects.get(pk=id)
   if request.method == 'POST':
    
       form = Reviewal_Form(request.POST, instance=q)  
       if form.is_valid():
           form.save()
       return HttpResponseRedirect(request.path)    
   else:
       form = Reviewal_Form(instance=q)          

   my_context = Context({'reviewaledit':q,'form':form,'user':request.user})
    
   return render_to_response ('Hospital/edit_reviewaldetails.html',my_context)  




class Lab_Form(ModelForm):
      class Meta:
         model=Test
         exclude=["LabTechnician"]

@csrf_exempt
@login_required
def lab_details(request):
    current_user = request.user
    labtec= LabTechnician.objects.get(user = current_user)
    thislab=LabTechnician.objects.get(user= current_user)
    status=False
    if request.method == 'POST':
        userinstance=Test(LabTechnician=thislab)
      	print "User submitted data"
	form = Lab_Form(request.POST, request.FILES,instance=userinstance) 
        if form.is_valid():
	    
            print "It validated"
            form.save()
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        form = Lab_Form()
    return render_to_response('Hospital/lab_page.html',{'form':form,'user':request.user,'labtec':labtec})




@csrf_exempt
@login_required
def edit_labdetails(request,id):
   q=Test.objects.get(pk=id)
   if request.method == 'POST':
    
       form = Lab_Form(request.POST, instance=q)  
       if form.is_valid():
           form.save()

       return HttpResponseRedirect(request.path)    
   else:
       form = Lab_Form(instance=q)          

   my_context = Context({'labedit':q,'form':form,'user':request.user})
    
   return render_to_response ('Hospital/edit_labdetails.html',my_context)  

@csrf_exempt
@login_required
def particular_patient(request, id,showComments=False):
   patient=Patient.objects.get(ODP_number=id)
   p=Patient.objects.filter(ODP_number__contains=patient)|Patient.objects.filter(first_name__contains=patient)|Patient.objects.filter(last_name__contains=patient)|Patient.objects.filter(gender__contains=patient)
   t = loader.get_template('Hospital/particular_patient.html')
   c = Context({
'patient': patient,'patient_list':p,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def particular_patient_diagnosis(request, id,showComments=False):
   patient=Patient.objects.get(ODP_number=id)
   diagnosiss=patient.diagnosiss.all()
   t = loader.get_template('Hospital/particular_patient_diagnosis.html')
   c = Context({
'patient': patient,'diagnosiss':diagnosiss,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def particular_patient_prescription(request, id,showComments=False):
   diagnosis=Diagnosis.objects.get(pk=id)
   prescriptions=diagnosis.prescriptions.all()
   t = loader.get_template('Hospital/particular_patient_prescription.html')
   c = Context({
'diagnosis':diagnosis,'prescriptions':prescriptions,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def particular_patient_lab(request, id,showComments=False):
   diagnosis=Diagnosis.objects.get(pk=id)
   labs=diagnosis.labs.all()
   t = loader.get_template('Hospital/particular_patient_lab.html')
   c = Context({
'diagnosis': diagnosis,'labs':labs
})
   return HttpResponse(t.render(c))




@csrf_exempt
@login_required
def particular_patient_reviewal(request, id,showComments=False):
   prescriptions=Prescription.objects.get(pk=id)
   reviewals=prescriptions. reviewals.all()
   t = loader.get_template('Hospital/particular_patient_reviewal.html')
   c = Context({
'prescriptions': prescriptions,'reviewals':reviewals,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def patientpage_diagnosislist(request):
   current_user = request.user
   patient= Patient.objects.get(user = current_user)
   diagnosiss=patient.diagnosiss.all()
   t = loader.get_template('Hospital/patientpage_diagnosislist.html')
   c = Context({
'patient': patient,'diagnosiss':diagnosiss,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def patientpage_diagnosislist(request):
   current_user = request.user
   patient= Patient.objects.get(user = current_user)
   diagnosiss=patient.diagnosiss.all()
   t = loader.get_template('Hospital/patientpage_diagnosislist.html')
   c = Context({
'patient': patient,'diagnosiss':diagnosiss,'user':request.user
})
   return HttpResponse(t.render(c))


@csrf_exempt
@login_required
def patientpage_prescriptionlist(request):
   current_user = request.user
   patient= Patient.objects.get(user = current_user)
   sss=patient.sss.all()
   t = loader.get_template('Hospital/patientpage_prescriptionlist.html')
   c = Context({
'patient': patient,'sss':sss,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def patientpage_labtestlist(request):
   current_user = request.user
   patient= Patient.objects.get(user = current_user)
   testss=patient.testss.all()
   t = loader.get_template('Hospital/patientpage_labtestlist.html')
   c = Context({
'patient': patient,'testss':testss,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def patientpage_reviewallist(request):
   current_user = request.user
   patient= Patient.objects.get(user = current_user)
   Reviewalss=patient.Reviewalss.all()
   t = loader.get_template('Hospital/patientpage_reviewallist.html')
   c = Context({
'patient': patient,'Reviewalss':Reviewalss,'user':request.user
})
   return HttpResponse(t.render(c))


@csrf_exempt
@login_required
def particular_viewpres(request, id,showComments=False):
   patient=Patient.objects.get(ODP_number=id)
   sss=patient.sss.all()
   t = loader.get_template('Hospital/particular_viewpres.html')
   c = Context({
'patient': patient,'sss':sss,'user':request.user
})
   return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def particular_viewlab(request, id,showComments=False):
   current_user = request.user
   patient=Patient.objects.get(ODP_number=id)
   testss=patient.testss.all()
   t = loader.get_template('Hospital/particular_viewlab.html')
   c = Context({
'patient': patient,'testss':testss,'user':request.user
})
   return HttpResponse(t.render(c))


@csrf_exempt
@login_required
def particular_viewvitals(request):
   current_user = request.user
   patient= Patient.objects.get(user = current_user)
   vitalsss=patient.vitalsss.all()
   t = loader.get_template('Hospital/particular_viewvitals.html')
   c = Context({
'patient': patient,'vitalsss':vitalsss,'user':request.user
})
   return HttpResponse(t.render(c))




@csrf_exempt
@login_required
def particular_viewreview(request, id,showComments=False):
   patient=Patient.objects.get(ODP_number=id)
   Reviewalss=patient.Reviewalss.all()
   t = loader.get_template('Hospital/particular_viewreview.html')
   c = Context({
'patient': patient,'Reviewalss':Reviewalss,'user':request.user
})
   return HttpResponse(t.render(c))

class Comment_Form(ModelForm):
      class Meta:
         model=Comment
         exclude=["doctor"]

@csrf_exempt
@login_required
def post_comment(request):
    current_user = request.user
    doc= Doctor.objects.get(user = current_user)
    thisdoc=Doctor.objects.get(user= current_user)
    status=False
    if request.method == 'POST':
        userinstance=Comment(doctor=thisdoc)
      	print "User submitted data"
	form = Comment_Form(request.POST, request.FILES,instance=userinstance) 
        if form.is_valid():
	    
            print "It validated"
            form.save()
            return HttpResponseRedirect('/sentreport_list')
    else:
	print "It's not post"
        form =Comment_Form()
    return render_to_response('Hospital/Report_Post.html',{'form':form,'user':request.user,'doc':doc})

@csrf_exempt
@login_required
def sentreport_list(request):
    current_user = request.user
    doc= Doctor.objects.get(user = current_user)
    comment_list = Comment.objects.all()
    t = loader.get_template("Hospital/post_reportlist.html")
    c = Context({ 'comment_list': comment_list,'user':request.user})
    return HttpResponse(t.render(c))


@csrf_exempt
@login_required
def receivedreport_list(request):
    current_user = request.user
    doc= Doctor.objects.get(user = current_user)
    report_list = Report.objects.all()
    t = loader.get_template("Hospital/receivedreport_list.html")
    c = Context({ 'report_list': report_list,'user':request.user})
    return HttpResponse(t.render(c))




class Report_Form(ModelForm):
      class Meta:
         model=Report
         exclude=["patient"]


@csrf_exempt
@login_required
def patientpost_report(request):
    current_user = request.user
    pat= Patient.objects.get(user = current_user)
    thispat=Patient.objects.get(user= current_user)
    status=False
    if request.method == 'POST':
        userinstance=Report(patient=thispat)
      	print "User submitted data"
	form = Report_Form(request.POST, request.FILES,instance=userinstance) 
        if form.is_valid():
	    
            print "It validated"
            form.save()
            return HttpResponseRedirect('/report_list')
    else:
	print "It's not post"
        form =Report_Form()
    return render_to_response('Hospital/PatientReport_Post.html',{'form':form,'user':request.user,'pat':pat})



@csrf_exempt
@login_required
def particular_Vitals(request, id,showComments=False):
   current_user = request.user
   patient=Patient.objects.get(ODP_number=id)
   vitalsss=patient.vitalsss.all()
   t = loader.get_template('Hospital/Vitals_list.html')
   c = Context({
'patient': patient,'vitalsss':vitalsss,'user':request.user
})
   return HttpResponse(t.render(c))


@csrf_exempt
@login_required
def report_list(request):
    current_user = request.user
    pat= Patient.objects.get(user = current_user)
    report_list = Report.objects.all()
    t = loader.get_template("Hospital/patientpost_reportlist.html")
    c = Context({ 'report_list': report_list,'user':request.user})
    return HttpResponse(t.render(c))

@csrf_exempt
@login_required
def patientreceivedcomment_list(request):
    current_user = request.user
    patient= Patient.objects.get(user = current_user)
    comment_list = Comment.objects.all()
    t = loader.get_template("Hospital/patientreceivedcomment_list.html")
    c = Context({ 'comment_list': comment_list,'user':request.user})
    return HttpResponse(t.render(c))


class Vital_Form(ModelForm):
      class Meta:
         model=Vitals
         exclude=["nurse"]
         
         
@login_required         
@csrf_exempt
def Vitals_details(request):
    current_user = request.user
    nurse= Nurse.objects.get(user = current_user)
    thisnurse=Nurse.objects.get(user= current_user)
    status=False
    if request.method == 'POST':
        userinstance=Vitals(nurse=thisnurse)
      	print "User submitted data"
	theform = Vital_Form(request.POST, request.FILES,instance=userinstance) 
        if theform.is_valid():
            print "It validated"
            theform.save()
            return HttpResponseRedirect('')
    else:
	print "It's not post"
        theform =Vital_Form()
    return render_to_response('Hospital/Vitals.html',{'form':theform,'user':request.user})




@csrf_exempt
@login_required
def edit_vitaldetails(request,id):
   q=Vitals.objects.get(pk=id)
   if request.method == 'POST':
    
       form = Vital_Form(request.POST, instance=q)  
       if form.is_valid():
           user = request.user.id
           form.save()
       return HttpResponseRedirect(request.path)    
   else:
       form = Vital_Form(instance=q)
   my_context = Context({'vitalsedit':q,'form':form,'user':request.user})
    
   return render_to_response ('Hospital/edit_vitalsdetails.html',my_context)





















































































