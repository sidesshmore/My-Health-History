from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    uid = serializers.CharField(max_length=12, allow_null=True, allow_blank=True)
    name = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    dob = serializers.DateField(allow_null=True)
    gender = serializers.CharField(max_length=1, allow_null=True, allow_blank=True)
    phone = serializers.CharField(max_length=10, allow_null=True, allow_blank=True)
    email = serializers.EmailField(allow_null=True, allow_blank=True)
    street = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    district = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    state = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    pincode = serializers.CharField(max_length=6, allow_null=True, allow_blank=True)

    class Meta:
        model = Patient
        fields = '__all__'

class LabSerializer(serializers.ModelSerializer):
    lab_id = serializers.CharField(max_length=12, allow_null=True, allow_blank=True)
    lab_name = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    lab_address = serializers.CharField(max_length=200, allow_null=True, allow_blank=True)
    lab_phone = serializers.CharField(max_length=15, allow_null=True, allow_blank=True)

    class Meta:
        model = Lab
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    doctor_id = serializers.CharField(max_length=9, allow_null=True, allow_blank=True)
    doctor_name = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    degree = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    doctor_number = serializers.CharField(max_length=15, allow_null=True, allow_blank=True)

    class Meta:
        model = Doctor
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    report_no = serializers.IntegerField(source='report_no', read_only=True)
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    lab = serializers.PrimaryKeyRelatedField(queryset=Lab.objects.all())
    date = serializers.DateField()
    test_name = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    report_pdf = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        model = Reports
        fields = '__all__'


class ReportDetailsSerializer(serializers.ModelSerializer):
    lab_name = serializers.SerializerMethodField()  

    class Meta:
        model = Reports
        fields = ['date', 'test_name', 'lab', 'lab_name', 'report_pdf'] 

    def get_lab_name(self, obj):
        return obj.lab.lab_name

    

class PrescriptionSerializer(serializers.ModelSerializer):
    prescription_link = serializers.URLField(max_length=500, allow_null=True, allow_blank=True)
    test_required = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = Prescription
        fields = '__all__'

class CreateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'


class UpdateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ['test_name', 'report_pdf']

class DeleteReportSerializer(serializers.Serializer):
    report_no = serializers.IntegerField()
