# from django.urls import path
# from .views import BannerListView, YouTubeLinkListView, HealthPackageListView, HealthPackageBookingView, SubscriptionListView

# urlpatterns = [
#     path('home/banner/', BannerListView.as_view(), name='banner-list'),
#     path('home/youtube-links/', YouTubeLinkListView.as_view(), name='youtube-link-list'),
#     path('home/health-packages/', HealthPackageListView.as_view(), name='health-package-list'),
#     path('home/health-packages/book/', HealthPackageBookingView.as_view(), name='health-package-booking'),
#     path('home/subscriptions/', SubscriptionListView.as_view(), name='subscription-list'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # Banner
    path('banners/', views.BannerListView.as_view(), name='banner-list'),
    path('banners/create/', views.BannerCreateView.as_view(), name='banner-create'),
    path('banners/<int:pk>/', views.BannerDetailView.as_view(), name='banner-detail'),
    
    # YouTube Link
    path('youtube-links/', views.YouTubeLinkListView.as_view(), name='youtube-link-list'),
    path('youtube-links/create/', views.YouTubeLinkCreateView.as_view(), name='youtube-link-create'),
    path('youtube-links/<int:pk>/', views.YouTubeLinkDetailView.as_view(), name='youtube-link-detail'),
    
    # Health Package
    path('health-packages/', views.HealthPackageListView.as_view(), name='health-package-list'),
    path('health-packages/create/', views.HealthPackageCreateView.as_view(), name='health-package-create'),
    path('health-packages/<int:pk>/', views.HealthPackageDetailView.as_view(), name='health-package-detail'),
    
    # Health Package Booking (Subscription)
    path('book-package/', views.HealthPackageBookingView.as_view(), name='health-package-book'),
    
    # Subscription
    path('subscriptions/', views.SubscriptionListView.as_view(), name='subscription-list'),
    path('subscriptions/<int:pk>/', views.SubscriptionDetailView.as_view(), name='subscription-detail'),
]
