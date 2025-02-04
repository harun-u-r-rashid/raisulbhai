from rest_framework import serializers
from .models import Banner, YouTubeLink, HealthPackage, Subscription

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class YouTubeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeLink
        fields = '__all__'

class HealthPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthPackage
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
