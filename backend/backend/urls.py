from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('api/medical/', include('medical.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/cdss/', include('cdss.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/imaging/', include('imaging.urls')),
]
