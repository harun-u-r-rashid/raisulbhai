from rest_framework import serializers
from .models import CaregiverType, CaregiverPackage, CaregiverPackageList

class CaregiverTypeSerializer(serializers.ModelSerializer):
    packages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CaregiverType
        fields = '__all__'

class CaregiverPackageSerializer(serializers.ModelSerializer):
    package_lists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CaregiverPackage
        fields = '__all__'

class CaregiverPackageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaregiverPackageList
        fields = '__all__'
