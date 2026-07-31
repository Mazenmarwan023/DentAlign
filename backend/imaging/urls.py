from django.urls import path
from .views import UploadDicomView, ProcessDicomView

urlpatterns = [
    path('upload/', UploadDicomView.as_view(), name='dicom-upload'),
    path('process/', ProcessDicomView.as_view(), name='dicom-process'),
]
