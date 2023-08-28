from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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


