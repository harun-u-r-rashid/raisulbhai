from rest_framework import generics
from .models import CaregiverType, CaregiverPackage, CaregiverPackageList
from .serializers import CaregiverTypeSerializer, CaregiverPackageSerializer, CaregiverPackageListSerializer

# Caregiver Type Views
class CaregiverTypeListView(generics.ListCreateAPIView):
    queryset = CaregiverType.objects.all()
    serializer_class = CaregiverTypeSerializer

class CaregiverTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaregiverType.objects.all()
    serializer_class = CaregiverTypeSerializer

# Caregiver Package Views
class CaregiverPackageListView(generics.ListCreateAPIView):
    queryset = CaregiverPackage.objects.all()
    serializer_class = CaregiverPackageSerializer

class CaregiverPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaregiverPackage.objects.all()
    serializer_class = CaregiverPackageSerializer

# Caregiver Package List Views
class CaregiverPackageListListView(generics.ListCreateAPIView):
    queryset = CaregiverPackageList.objects.all()
    serializer_class = CaregiverPackageListSerializer

class CaregiverPackageListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaregiverPackageList.objects.all()
    serializer_class = CaregiverPackageListSerializer
