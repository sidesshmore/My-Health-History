from django.contrib import admin
from .models import *
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    sortable_by = 'uid'  # field 'id' sorted by descending order
    search_fields = ['uid','name', 'email']  # list of fields search in admin table
    list_display = ('uid', 'name', 'dob', 'email', 'phone', 'gender')
    list_display_links = ['uid']
admin.site.register(Patient,PatientAdmin)

class LabAdmin(admin.ModelAdmin):
    sortable_by = 'lab_id'  # field 'id' sorted by descending order
    search_fields = ['lab_id','lab_name', 'phone']  # list of fields search in admin table
    list_display = ('lab_id', 'lab_name', 'lab_address', 'lab_phone')
    list_display_links = ['lab_id']
admin.site.register(Lab,LabAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'doctor_name', 'degree', 'doctor_number')
    search_fields = ['doctor_id', 'doctor_name', 'degree', 'doctor_number']
    list_display_links = ['doctor_id']
admin.site.register(Doctor, DoctorAdmin)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_no', 'patient', 'lab', 'date', 'test_name')
    search_fields = ['report_no', 'patient__name', 'lab__lab_name', 'test_name']
    list_filter = ('date', 'lab')
    list_display_links = ['report_no']
    list_select_related = ('patient', 'lab')
admin.site.register(Reports, ReportAdmin)
    
