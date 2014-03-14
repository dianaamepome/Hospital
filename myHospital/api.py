from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from models import *
from tastypie.authorization import DjangoAuthorization


class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    allowed_methods = ['get', 'post']



class PatientResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Patient.objects.all()
        resource_name = 'patient'
        authorization = DjangoAuthorization()
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }


class VitalsResource(ModelResource):
    patient = fields.ForeignKey(PatientResource, 'patient')
    class Meta:
        queryset = Vitals.objects.all()
        resource_name = 'vitals'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }


class DiagnosisResource(ModelResource):
    patient = fields.ForeignKey(PatientResource, 'patient')
    class Meta:
        queryset = Diagnosis.objects.all()
        resource_name = 'diagnosis'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }

class PrescriptionResource(ModelResource):
    patient = fields.ForeignKey(PatientResource, 'patient')
    class Meta:
        queryset = Prescription.objects.all()
        resource_name = 'prescription'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }

class ReviewalsResource(ModelResource):
    patient = fields.ForeignKey(PatientResource, 'patient')
    class Meta:
        queryset = Reviewals.objects.all()
        resource_name = 'reviewals'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }


class TestResource(ModelResource):
    patient = fields.ForeignKey(PatientResource, 'patient')
    class Meta:
        queryset = Test.objects.all()
        resource_name = 'test'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }


class DoctorResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Doctor.objects.all()
        resource_name = 'doctor'
        allowed_methods = ['get']
        filtering = {
            'id': ALL,
            }
