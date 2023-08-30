from django.urls import path
from .views import *

urlpatterns = [
    path('api/patient/<str:uid>/', PatientReportAPI.as_view(), name='patient-report-api'),

    path('api/lab/<str:lab_id>/reports/', LabReportsAPI.as_view(), name='lab-reports'),

    # API endpoint for patients to view their reports
    path('api/patient/<str:patient_uid>/reports/', PatientReportsAPI.as_view(), name='patient-reports'),

    # API endpoint for searching and filtering reports
    path('api/reports/search/', ReportSearchFilterAPI.as_view(), name='report-search'),
]


# GET /api/reports/search/?test_name=<test_name>&patient_name=<patient_name>&lab_name=<lab_name>&start_date=<start_date>&end_date=<end_date>
