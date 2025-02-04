from django.contrib import admin
from .models import CaregiverType, CaregiverPackage, CaregiverPackageList

admin.site.register(CaregiverType)
admin.site.register(CaregiverPackage)
admin.site.register(CaregiverPackageList)
