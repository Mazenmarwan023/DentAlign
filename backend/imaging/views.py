from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.conf import settings
from .models import DicomImage
from .serializers import DicomImageSerializer
import SimpleITK as sitk
import pydicom
import os
import io
import base64
import numpy as np

class UploadDicomView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = DicomImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProcessDicomView(APIView):
    def post(self, request):
        """
        Apply SimpleITK filters to a DICOM file.
        Expects: 'file_id' and 'filter_type' (sharpen, smooth, noise_reduction)
        Returns: Base64 encoded PNG of the processed slice (middle slice usually)
        """
        file_id = request.data.get('file_id')
        filter_type = request.data.get('filter_type')
        
        try:
            dicom_record = DicomImage.objects.get(id=file_id)
            file_path = dicom_record.file.path
            
            # Read DICOM Image using SimpleITK
            image = sitk.ReadImage(file_path)
            
            # Apply Filter
            if filter_type == 'sharpen':
                # Lapuncian Sharpening
                image = sitk.LaplacianSharpening(image)
            elif filter_type == 'smooth':
                # Gaussian Smoothing
                image = sitk.DiscreteGaussian(image, variance=1.0)
            elif filter_type == 'noise_reduction':
                # Curvature Flow
                image = sitk.CurvatureFlow(image, timeStep=0.125, numberOfIterations=5)
            
            # For visualization, we need to convert to an array and likely pick a slice if it's 3D
            # SimpleITK image to numpy
            img_array = sitk.GetArrayFromImage(image)
            
            # Handle dimensions (assuming 3D or 2D)
            if img_array.ndim == 3:
                # Take middle slice
                slice_idx = img_array.shape[0] // 2
                img_slice = img_array[slice_idx, :, :]
            else:
                img_slice = img_array
                
            # Normalize to 0-255 for PNG display
            img_slice = img_slice.astype(float)
            img_slice = (img_slice - img_slice.min()) / (img_slice.max() - img_slice.min()) * 255.0
            img_slice = img_slice.astype(np.uint8)
            
            # Convert to PIL and then Base64
            from PIL import Image
            pil_img = Image.fromarray(img_slice)
            buffered = io.BytesIO()
            pil_img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return Response({
                'success': True,
                'image': f"data:image/png;base64,{img_str}"
            })
            
        except DicomImage.DoesNotExist:
             return Response({'error': 'File not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
