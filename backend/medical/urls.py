from django.urls import path
from . import views

app_name = 'medical'

urlpatterns = [
    path('records/', views.MedicalRecordListView.as_view(), name='record_list'),
    path('records/<uuid:pk>/', views.MedicalRecordDetailView.as_view(), name='record_detail'),
    path('diagnoses/', views.DiagnosisListView.as_view(), name='diagnosis_list'),
    path('treatments/', views.TreatmentListView.as_view(), name='treatment_list'),
]
