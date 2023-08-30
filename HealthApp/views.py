from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, filters
from django.http import Http404
from .models import *
from .serailizers import *

from django.db.models import F

class PatientReportAPI(APIView):
    def get_patient(self, uid):
        try:
            return Patient.objects.get(uid=uid)
        except Patient.DoesNotExist:
            raise Http404("Patient does not exist")

    def get(self, request, uid):
        try:
            patient = self.get_patient(uid)
            
            # Fetch the reports, ordering them by date in descending order (latest first)
            reports = Reports.objects.filter(patient=patient).order_by('-date')
            
            # Serialize the reports with the updated serializer
            report_details = ReportDetailsSerializer(reports, many=True).data
            
            response_data = {
                "uid": patient.uid,
                "name": patient.name,
                "reports": report_details,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LabReportsAPI(generics.ListAPIView):
    serializer_class = ReportDetailsSerializer

    def get_queryset(self):
        lab_id = self.kwargs['lab_id']  # Assuming you pass lab_id as a URL parameter
        return Reports.objects.filter(lab__lab_id=lab_id).order_by('-date')
    
class PatientReportsAPI(generics.ListAPIView):
    serializer_class = ReportDetailsSerializer

    def get_queryset(self):
        patient_uid = self.kwargs['patient_uid']  # Assuming you pass patient_uid as a URL parameter
        return Reports.objects.filter(patient__uid=patient_uid).order_by('-date')
    

from rest_framework import generics, filters
from .models import Reports


class ReportSearchFilterAPI(generics.ListAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportDetailsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['test_name', 'patient__name', 'lab__lab_name', 'date']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by test name, patient name, lab name, and date range
        test_name = self.request.query_params.get('test_name')
        if test_name:
            queryset = queryset.filter(test_name__icontains=test_name)

        patient_name = self.request.query_params.get('patient_name')
        if patient_name:
            queryset = queryset.filter(patient__name__icontains=patient_name)

        lab_name = self.request.query_params.get('lab_name')
        if lab_name:
            queryset = queryset.filter(lab__lab_name__icontains=lab_name)

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset


