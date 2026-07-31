from rest_framework import generics, permissions
from staff.models import MedicalRecord, Diagnosis, Treatment
from staff.serializers import MedicalRecordSerializer, DiagnosisSerializer, TreatmentSerializer

class MedicalRecordListView(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all().order_by('-record_date')
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicalRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

class DiagnosisListView(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.all().order_by('-diagnosed_at')
    serializer_class = DiagnosisSerializer
    permission_classes = [permissions.IsAuthenticated]

class TreatmentListView(generics.ListCreateAPIView):
    queryset = Treatment.objects.all().order_by('-created_at')
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.IsAuthenticated]
