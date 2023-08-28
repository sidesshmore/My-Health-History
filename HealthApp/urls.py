from django.urls import path
from .views import PatientReportAPI

urlpatterns = [
    path('api/patient/<str:uid>/', PatientReportAPI.as_view(), name='patient-report-api'),
]
