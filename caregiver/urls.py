from django.urls import path
from .views import (
    CaregiverTypeListView, CaregiverTypeDetailView,
    CaregiverPackageListView, CaregiverPackageDetailView,
    CaregiverPackageListListView, CaregiverPackageListDetailView
)

urlpatterns = [
    # Caregiver Types
    path('types/', CaregiverTypeListView.as_view(), name='caregiver-type-list'),
    path('types/<int:pk>/', CaregiverTypeDetailView.as_view(), name='caregiver-type-detail'),

    # Caregiver Packages (Filtered by type)
    path('packages/', CaregiverPackageListView.as_view(), name='caregiver-package-list'),
    path('packages/<int:pk>/', CaregiverPackageDetailView.as_view(), name='caregiver-package-detail'),

    # Caregiver Package Lists (Filtered by package)
    path('package-lists/', CaregiverPackageListListView.as_view(), name='caregiver-package-list-list'),
    path('package-lists/<int:pk>/', CaregiverPackageListDetailView.as_view(), name='caregiver-package-list-detail'),
]
