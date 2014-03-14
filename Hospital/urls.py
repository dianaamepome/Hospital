from django.conf.urls import patterns, include, url
from django.conf import settings
from tastypie.api import Api
from myHospital.api import UserResource, PatientResource,VitalsResource,DiagnosisResource,PrescriptionResource,ReviewalsResource,  TestResource,DoctorResource
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register( PatientResource())
v1_api.register( VitalsResource())
v1_api.register( DiagnosisResource())
v1_api.register( PrescriptionResource())
v1_api.register( ReviewalsResource())
v1_api.register( TestResource())
v1_api.register( DoctorResource())

urlpatterns = patterns('',



    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myHospital.views.frontpage'),
    url(r'^homepage/$', 'myHospital.views.frontpage'),
    url(r'^patient_page$', 'myHospital.views.patient_page'),
    url(r'^patientreceivedcomment_list/$', 'myHospital.views.patientreceivedcomment_list'),
    url(r'^doctor_page/$', 'myHospital.views.doctor_page'),
url(r'^doctor_list$','myHospital.views.doctor_list'),
    url(r'^doctorreg$','myHospital.views.doctorreg'),
    url(r'^Registrarreg$','myHospital.views.Registrarreg'),
url(r'^registrar_page$','myHospital.views.registrar_page'),
url(r'^nursereg$','myHospital.views.nursereg'),
url(r'^LabTechnicianreg$','myHospital.views.LabTechnicianreg'),
url(r'^reg_pat_admin$','myHospital.views.reg_pat_admin'),
    url(r'^patientreg$','myHospital.views.patientreg'),
    url(r'^post_comment$','myHospital.views.post_comment'),
    url(r'^sentreport_list$','myHospital.views.sentreport_list'),
    url(r'^report_list$','myHospital.views.report_list'),
url(r'^nurse_page$','myHospital.views.nurse_page'),
url(r'^labtec_page$','myHospital.views.labtec_page'),




    url(r'^patientpost_report$','myHospital.views.patientpost_report'),
    url(r'^receivedreport_list','myHospital.views.receivedreport_list'),
    url(r'^diagnosis_details/$', 'myHospital.views.diagnosis_details'),

url(r'^patient_list/(?P<id>\d+)/edit/$','myHospital.views.edit_patientreg'),
url(r'^patient_list$','myHospital.views.patient_list'),
url(r'^healthfacility_list$','myHospital.views.healthfacility_list'),
url(r'^doctor_list$','myHospital.views.doctor_list'),
url(r'^/doctor_list$','myHospital.views.doctor_list'),
url(r'^healthfacility_list/search/(?P<term>.*?)$','myHospital.views.healthfacilitylist_search'),
#url(r'^doctor_page/patient_list/particular_patient$','myHospital.views.particular_patient'),
#url(r'^particular_patient/(?P<id>\d+)/$', 'myHospital.views.particular_patient'),
url(r'^particular_patient/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_patient'),
url(r'^particular_patient_diagnosis/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_patient_diagnosis'),

url(r'^particular_patient_diagnosis/(?P<id>\d+)/edit/$','myHospital.views.edit_diagnosisdetails'),

url(r'^particular_patient_diagnosis/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_patient_prescription'),

url(r'^particular_viewpres/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_viewpres'),
url(r'^particular_viewlab/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_viewlab'),
url(r'^particular_viewreview/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_viewreview'),
url(r'^particular_Vitals/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_Vitals'),
url(r'^particular_viewvitals/', 'myHospital.views.particular_viewvitals'),

url(r'^edit_vitaldetails/(?P<id>\d+)/edit/$','myHospital.views.edit_vitaldetails'),
url(r'^particular_patient_prescription/(?P<id>\d+)/edit/$','myHospital.views.edit_prescriptiondetails'),
url(r'^particular_patient_prescription/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.particular_patient_reviewal'),
url(r'^particular_patient_reviewal/(?P<id>\d+)/edit/$','myHospital.views.edit_reviewaldetails'),
url(r'^particular_patient_lab/(?P<id>\d+)/edit/$', 'myHospital.views.particular_patient_lab'),
url(r'^particular_patient_diagnosis/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'myHospital.views.edit_labdetails'),


url(r'^particular_patient/(?P<id>\d+)/((?P<showComments>.*)/diagnosis_details)?$', 'myHospital.views.diagnosis_details'),

url(r'^prescription_details/$', 'myHospital.views.prescription_details'),
url(r'^lab_details/', 'myHospital.views.lab_details'),
url(r'^reviewal_details/', 'myHospital.views.reviewal_details'),
url(r'^Vitals_details/', 'myHospital.views.Vitals_details'),

url(r'^doctor_page/patient_list/particular_patient/prescription_details$','myHospital.views.prescription_details'),
url(r'^doctor_page/patient_list/particular_patient/reviewal_details$','myHospital.views.reviewal_details'),
url(r'^doctor_page/patient_list/particular_patient/lab_details$','myHospital.views.lab_details'),
url(r'^doctor_page/patient_list/search/(?P<term>.*?)$','myHospital.views.patientlist_search'),
url(r'^doctor_page/prescription_list$','myHospital.views.prescription_list'),
url(r'^doctor_page/prescription_list/search/(?P<term>.*?)$','myHospital.views.prescriptionlist_search'),
url(r'^doctor_page/lab_list$','myHospital.views.lab_list'),
url(r'^doctor_page/lab_list/search/(?P<term>.*?)$','myHospital.views.lablist_search'),
url(r'^doctor_page/diagnosis_list$','myHospital.views.diagnosis_list'),
url(r'^doctor_page/diagnosis_list/search/(?P<term>.*?)$','myHospital.views.diagnosislist_search'),
url(r'^doctor_page/reviewal_list$','myHospital.views.reviewal_list'),
url(r'^doctor_page/reviewal_list/search/(?P<term>.*?)$','myHospital.views.reviewallist_search'),

    url(r'^contact_us$','myHospital.views.contact_us'),
url(r'^about_us$','myHospital.views.about_us'),

    url(r'^patientapp/', include('patientapp.urls')),
    url(r'^healthprovider/', include('healthprovider.urls')),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),

url(r'^patientpage_diagnosislist$', 'myHospital.views.patientpage_diagnosislist'),
url(r'^patientpage_prescriptionlist$', 'myHospital.views.patientpage_prescriptionlist'),
url(r'^patientpage_labtestlist$', 'myHospital.views.patientpage_labtestlist'),
url(r'^patientpage_reviewallist$', 'myHospital.views.patientpage_reviewallist'),
url(r'^django-session-idle-timeout/', include('django-session-idle-timeout.urls')),
url(r"^reminders/", include("reminders.urls")),
(r'^api/', include(v1_api.urls)),

)


