from django.forms import ModelForm
from django.db import models
from django.db.models.signals import post_save
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import datetime


class HealthFacility(models.Model):
      HealthFacility_ID = models.IntegerField(max_length = 10,unique=True)
      HealthFacility_name = models.CharField(max_length = 255)
      HealthFacility_Details = models.CharField(max_length = 255)
      phone_number = models.CharField(max_length = 10)
      email = models.EmailField(unique=True)
      Address= models.CharField(max_length = 255)
      country = models.CharField(max_length = 255)
      city= models.CharField(max_length = 255)
      
      def __unicode__(self):

            return str(self.HealthFacility_ID)

class Doctor(models.Model):
      user = models.OneToOneField(User,related_name='doctor')
      Doctor_ID = models.CharField(max_length = 10,unique=True)
      first_name = models.CharField(max_length = 255)
      last_name = models.CharField(max_length = 255)
      GENDER_CHOICES = (('Male','Male'),('Female','Female'),)
      gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
      date_of_birth = models.DateField(default = "DD-MM-YYYY")
      Specialization= models.CharField(max_length = 255)
      phone_number = models.CharField(max_length = 10)
      email = models.EmailField(unique=True)
      Address= models.CharField(max_length = 255)
      country = models.CharField(max_length = 255)
      city= models.CharField(max_length = 255)
      healthfacility=models.ForeignKey(HealthFacility)
      def __unicode__(self):
            return str(self.Doctor_ID)


class Registrar(models.Model):
      user = models.OneToOneField(User,related_name='registrar')
      Registrar_ID = models.CharField(max_length = 10,unique=True)
      first_name = models.CharField(max_length = 255)
      last_name = models.CharField(max_length = 255)
      GENDER_CHOICES = (('Male','Male'),('Female','Female'),)
      gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
      date_of_birth = models.DateField(default = "DD-MM-YYYY")
      phone_number = models.CharField(max_length = 10)
      email = models.EmailField(unique=True)
      Address= models.CharField(max_length = 255)
      country = models.CharField(max_length = 255)
      city= models.CharField(max_length = 255)
      healthfacility=models.ForeignKey(HealthFacility)
      def __unicode__(self):
            return str(self.Registrar_ID)

class Nurse(models.Model):
      user = models.OneToOneField(User,related_name='Nurse')
      Nurse_ID = models.CharField(max_length = 10,unique=True)
      first_name = models.CharField(max_length = 255)
      last_name = models.CharField(max_length = 255)
      GENDER_CHOICES = (('Male','Male'),('Female','Female'),)
      gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
      date_of_birth = models.DateField(default = "DD-MM-YYYY")
      phone_number = models.CharField(max_length = 10)
      email = models.EmailField(unique=True)
      Address= models.CharField(max_length = 255)
      country = models.CharField(max_length = 255)
      city= models.CharField(max_length = 255)
      healthfacility=models.ForeignKey(HealthFacility)
      def __unicode__(self):
            return str(self.Nurse_ID)


class LabTechnician(models.Model):
      user = models.OneToOneField(User,related_name='LabTechnician')
      LabTechnician_ID = models.CharField(max_length = 10,unique=True)
      first_name = models.CharField(max_length = 255)
      last_name = models.CharField(max_length = 255)
      GENDER_CHOICES = (('Male','Male'),('Female','Female'),)
      gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
      date_of_birth = models.DateField(default = "DD-MM-YYYY")
      phone_number = models.CharField(max_length = 10)
      email = models.EmailField(unique=True)
      Address= models.CharField(max_length = 255)
      country = models.CharField(max_length = 255)
      city= models.CharField(max_length = 255)
      lab_facility_name=models.CharField(max_length = 255)
      def __unicode__(self):
            return str(self.LabTechnician_ID)




class Patient(models.Model):
      user = models.OneToOneField(User, unique=True)
      ODP_number = models.CharField(max_length = 10,unique=True)
      first_name = models.CharField(max_length = 255)
      last_name = models.CharField(max_length = 255)
      GENDER_CHOICES = (('Male','Male'),('Female','Female'),)
      gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
      date_of_birth = models.DateField(default = "DD-MM-YYYY")
      Occupation = models.CharField(max_length = 255)
      phone_number = models.IntegerField(max_length = 10)
      email = models.EmailField(unique=True)
      Address= models.CharField(max_length = 255)
      country = models.CharField(max_length = 255)
      city= models.CharField(max_length = 255) 
      special_requirements_or_alergies= models.CharField(max_length = 255)
   
      def __unicode__(self):
            return str(self.ODP_number)
     
class Vitals(models.Model):
     patient = models.ForeignKey(Patient,related_name='vitalsss')
     nurse=models.ForeignKey(Nurse,related_name='nursesss')
     Blood_Pressure =models.CharField(max_length = 255)
     Height =models.CharField(max_length = 255)
     Respirations =models.CharField(max_length = 255)
     Weight =models.CharField(max_length = 255)
     Temperature =models.CharField(max_length = 255)
     Pulse =models.CharField(max_length = 255)
     Oxygen_Saturation =models.CharField(max_length = 255)
     Vital_date=models.DateTimeField(auto_now=True)
     class Meta:
          ordering = ('-Vital_date',)

     def __unicode__(self):
          return self.Vital_date
     





class Diagnosis(models.Model): 
     patient = models.ForeignKey(Patient,related_name='diagnosiss')
     doctor=models.ForeignKey(Doctor,related_name='doctorsss')
     Diagnosis_ID = models.CharField(max_length = 10,unique=True)    
     Diagnosis_Majorcomplaints=models.CharField(max_length = 255)
     Diagnosis_Details=models.CharField(max_length = 255)
     Diagnosis_Referals=models.CharField(max_length = 255)
     Diagnosis_date=models.DateTimeField(auto_now=True)
     class Meta:
          ordering = ('-Diagnosis_ID',)

     def __unicode__(self):
          return self.Diagnosis_ID



class Prescription(models.Model):
     patient = models.ForeignKey(Patient,related_name='sss')
     diagnosis=models.ForeignKey(Diagnosis,related_name='prescriptions')
     doctor=models.ForeignKey(Doctor)
     Prescription_Details=models.CharField(max_length = 255)
     Prescription_date=models.DateField(auto_now=True)
     Medicine_Name=models.CharField(max_length = 255)
     Medicine_Doseage=models.CharField(max_length = 255)
     class Meta:
          ordering = ('-Prescription_date',)
     
     def __unicode__(self):
          return self.Prescription_date

class Report(models.Model):
       patient = models.ForeignKey(Patient,related_name='rep')
       doctor=models.ForeignKey(Doctor,related_name='repss')    
       title=models.CharField(max_length=60)
       body=models.TextField()
       Datecreated = models.DateTimeField(auto_now=True)
       class Meta:
             ordering = ('-Datecreated',)

       def __unicode__(self):
             return '[%s] %s' % (self.Datecreated.strftime('%Y-%m-%d %H:%M:%S'),self.title)





class Comment(models.Model):
       patient = models.ForeignKey(Patient,related_name='repsss')
       doctor=models.ForeignKey(Doctor,related_name='repssss')
       title=models.CharField(max_length=60)    
       body=models.TextField()
       Datecreated= models.DateTimeField(auto_now=True)
       class Meta:
          ordering = ('-Datecreated',)
       def __unicode__(self):
             return '[%s] %s' % (self.Datecreated.strftime('%Y-%m-%d %H:%M:%S'),self.title)



class Reviewals(models.Model):
     doctor=models.ForeignKey(Doctor,related_name='docss')
     patient = models.ForeignKey(Patient,related_name='Reviewalss')
     Reviewals_Date=models.DateField()
     Reviewals_Time=models.TimeField()
     class Meta:
          ordering = ('-Reviewals_Date',)
     
     def __unicode__(self):
          return self.Reviewals_Date

    
class Test(models.Model):
     patient = models.ForeignKey(Patient,related_name='testss')
     Diagnosis=models.ForeignKey(Diagnosis,related_name='labs')
     Test_Name=models.CharField(max_length = 255)
     Test_Result=models.CharField(max_length = 255)
     Test_date=models.DateTimeField(auto_now=True)
     LabTechnician=models.ForeignKey(LabTechnician,related_name='labtec')
     class Meta:
          ordering = ('-Test_date',)
     
     def __unicode__(self):
          return str(self.Test_date)




class DiagnosisAdmin(admin.ModelAdmin):
    list_display=('Diagnosis_Majorcomplaints','Diagnosis_Details','Diagnosis_date')
    search_fields =('Diagnosis_date','Diagnosis_Majorcomplaints','Diagnosis_Details')
    list_filter =('Diagnosis_date',)
    

class DiagnosisInline(admin.TabularInline):     
      model=Diagnosis


class PatientAdmin(admin.ModelAdmin):
    list_display=('gender','ODP_number','phone_number','first_name','last_name',)
    search_fields =('ODP_number','last_name','first_name')
    list_filter =('ODP_number',)
    inlines=[DiagnosisInline]



class DoctorAdmin(admin.ModelAdmin):
    list_display=('Doctor_ID','phone_number','first_name','last_name')
    search_fields =('Doctor_ID','last_name','first_name')
    list_filter =('Doctor_ID',)

class HealthFacilityAdmin(admin.ModelAdmin):
    list_display=('HealthFacility_ID','HealthFacility_name','phone_number',' country')
    search_fields =('HealthFacility_ID','HealthFacility_name','country')
    list_filter =('HealthFacility_ID',)

class TestAdmin(admin.ModelAdmin):
    list_display=('Test_Name','Test_Result','Test_date','LabTechnician')
    search_fields =('Test_Name','Test_Result')
    list_filter =('Test_Name',)

 
class ReviewalsAdmin(admin.ModelAdmin):
    list_display=('Reviewals_Date',)
    search_fields =('Reviewals_Date',)
    list_filter =('Reviewals_Date',)

class VitalsAdmin(admin.ModelAdmin):
    list_display=('Vital_date',)
    search_fields =('Vital_date',)
    list_filter =('Vital_date',)


class PrescriptionAdmin(admin.ModelAdmin):
    list_display=('Prescription_Details','Prescription_date','Medicine_Name','Medicine_Doseage')
    search_fields =('Prescription_Details','Medicine_Name')
    list_filter =('Prescription_date',)


admin.site.register(Reviewals,ReviewalsAdmin)
admin.site.register(Vitals,VitalsAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register(HealthFacility)
admin.site.register(Report)
admin.site.register(Comment)
admin.site.register(Diagnosis,DiagnosisAdmin)
admin.site.register(Prescription,PrescriptionAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(LabTechnician)
admin.site.register(Registrar)
admin.site.register(Nurse)
