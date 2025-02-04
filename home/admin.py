from django.contrib import admin
from .models import Banner, YouTubeLink, HealthPackage, Subscription

# Register models for the admin panel
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'link')
    search_fields = ('title', 'link')
    list_filter = ('title',)

@admin.register(YouTubeLink)
class YouTubeLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    search_fields = ('title', 'url')
    list_filter = ('title',)

@admin.register(HealthPackage)
class HealthPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'start_date', 'end_date')
    search_fields = ('user__username', 'package__name')
    list_filter = ('package', 'start_date', 'end_date')

