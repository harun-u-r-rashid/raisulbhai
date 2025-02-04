# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Banner, YouTubeLink, HealthPackage, Subscription
# from .serializers import BannerSerializer, YouTubeLinkSerializer, HealthPackageSerializer, SubscriptionSerializer

# class BannerListView(generics.ListAPIView):
#     queryset = Banner.objects.all()
#     serializer_class = BannerSerializer

# class YouTubeLinkListView(generics.ListAPIView):
#     queryset = YouTubeLink.objects.all()
#     serializer_class = YouTubeLinkSerializer

# class HealthPackageListView(generics.ListAPIView):
#     queryset = HealthPackage.objects.all()
#     serializer_class = HealthPackageSerializer

# class HealthPackageBookingView(generics.CreateAPIView):
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         user = request.user
#         package_id = request.data.get('package_id')

#         try:
#             package = HealthPackage.objects.get(id=package_id)
#         except HealthPackage.DoesNotExist:
#             return Response({'error': 'Health Package not found'}, status=status.HTTP_404_NOT_FOUND)

#         subscription = Subscription.objects.create(user=user, package=package, end_date='2025-12-31')
#         return Response(SubscriptionSerializer(subscription).data, status=status.HTTP_201_CREATED)

# class SubscriptionListView(generics.ListAPIView):
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Subscription.objects.filter(user=self.request.user)


# from rest_framework import generics, status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Banner, YouTubeLink, HealthPackage, Subscription
# from .serializers import BannerSerializer, YouTubeLinkSerializer, HealthPackageSerializer, SubscriptionSerializer

# # Banner Views
# class BannerListView(generics.ListAPIView):
#     queryset = Banner.objects.all()
#     serializer_class = BannerSerializer

# class BannerCreateView(generics.CreateAPIView):
#     queryset = Banner.objects.all()
#     serializer_class = BannerSerializer

# class BannerDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Banner.objects.all()
#     serializer_class = BannerSerializer

#     def destroy(self, request, *args, **kwargs):
#         try:
#             banner = self.get_object()
#         except Banner.DoesNotExist:
#             return Response({'error': 'Banner not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Proceed with deletion if the object exists
#         return super().destroy(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         try:
#             banner = self.get_object()
#         except Banner.DoesNotExist:
#             return Response({'error': 'Banner not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Update the object and return the updated data
#         return super().update(request, *args, **kwargs)

# # YouTube Link Views
# class YouTubeLinkListView(generics.ListAPIView):
#     queryset = YouTubeLink.objects.all()
#     serializer_class = YouTubeLinkSerializer

# class YouTubeLinkCreateView(generics.CreateAPIView):
#     queryset = YouTubeLink.objects.all()
#     serializer_class = YouTubeLinkSerializer

# class YouTubeLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = YouTubeLink.objects.all()
#     serializer_class = YouTubeLinkSerializer

#     def destroy(self, request, *args, **kwargs):
#         try:
#             youtube_link = self.get_object()
#         except YouTubeLink.DoesNotExist:
#             return Response({'error': 'YouTube Link not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Proceed with deletion if the object exists
#         return super().destroy(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         try:
#             youtube_link = self.get_object()
#         except YouTubeLink.DoesNotExist:
#             return Response({'error': 'YouTube Link not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Update the object and return the updated data
#         return super().update(request, *args, **kwargs)

# # Health Package Views
# class HealthPackageListView(generics.ListAPIView):
#     queryset = HealthPackage.objects.all()
#     serializer_class = HealthPackageSerializer

# class HealthPackageCreateView(generics.CreateAPIView):
#     queryset = HealthPackage.objects.all()
#     serializer_class = HealthPackageSerializer

# class HealthPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HealthPackage.objects.all()
#     serializer_class = HealthPackageSerializer

#     def destroy(self, request, *args, **kwargs):
#         try:
#             health_package = self.get_object()
#         except HealthPackage.DoesNotExist:
#             return Response({'error': 'Health Package not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Proceed with deletion if the object exists
#         return super().destroy(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         try:
#             health_package = self.get_object()
#         except HealthPackage.DoesNotExist:
#             return Response({'error': 'Health Package not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Update the object and return the updated data
#         return super().update(request, *args, **kwargs)

# # Health Package Booking View (Create Subscription)
# class HealthPackageBookingView(generics.CreateAPIView):
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         user = request.user
#         package_id = request.data.get('package_id')

#         try:
#             package = HealthPackage.objects.get(id=package_id)
#         except HealthPackage.DoesNotExist:
#             return Response({'error': 'Health Package not found'}, status=status.HTTP_404_NOT_FOUND)

#         subscription = Subscription.objects.create(user=user, package=package, end_date='2025-12-31')
#         return Response(SubscriptionSerializer(subscription).data, status=status.HTTP_201_CREATED)

# # Subscription Views
# class SubscriptionListView(generics.ListAPIView):
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Subscription.objects.filter(user=self.request.user)

# class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SubscriptionSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = Subscription.objects.all()

#     def destroy(self, request, *args, **kwargs):
#         try:
#             subscription = self.get_object()
#         except Subscription.DoesNotExist:
#             return Response({'error': 'Subscription not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Proceed with deletion if the object exists
#         return super().destroy(request, *args, **kwargs)

#     def update(self, request, *args, **kwargs):
#         try:
#             subscription = self.get_object()
#         except Subscription.DoesNotExist:
#             return Response({'error': 'Subscription not found'}, status=status.HTTP_404_NOT_FOUND)

#         # Update the object and return the updated data
#         return super().update(request, *args, **kwargs)


from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Banner, YouTubeLink, HealthPackage, Subscription
from .serializers import BannerSerializer, YouTubeLinkSerializer, HealthPackageSerializer, SubscriptionSerializer

# Common response messages
OBJECT_NOT_FOUND = "{} not found"
DELETE_SUCCESS = "{} deleted successfully"
UPDATE_SUCCESS = "{} updated successfully"
CREATE_SUCCESS = "{} created successfully"

# Banner Views
class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerCreateView(generics.CreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': CREATE_SUCCESS.format('Banner'), 'data': response.data}, status=status.HTTP_201_CREATED)

class BannerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Banner.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('Banner')}, status=status.HTTP_404_NOT_FOUND)
        super().destroy(request, *args, **kwargs)
        return Response({'message': DELETE_SUCCESS.format('Banner')}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Banner.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('Banner')}, status=status.HTTP_404_NOT_FOUND)
        response = super().update(request, *args, **kwargs)
        return Response({'message': UPDATE_SUCCESS.format('Banner'), 'data': response.data}, status=status.HTTP_200_OK)

# YouTube Link Views
class YouTubeLinkListView(generics.ListAPIView):
    queryset = YouTubeLink.objects.all()
    serializer_class = YouTubeLinkSerializer

class YouTubeLinkCreateView(generics.CreateAPIView):
    queryset = YouTubeLink.objects.all()
    serializer_class = YouTubeLinkSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': CREATE_SUCCESS.format('YouTube Link'), 'data': response.data}, status=status.HTTP_201_CREATED)

class YouTubeLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = YouTubeLink.objects.all()
    serializer_class = YouTubeLinkSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            self.get_object()
        except YouTubeLink.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('YouTube Link')}, status=status.HTTP_404_NOT_FOUND)
        super().destroy(request, *args, **kwargs)
        return Response({'message': DELETE_SUCCESS.format('YouTube Link')}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            self.get_object()
        except YouTubeLink.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('YouTube Link')}, status=status.HTTP_404_NOT_FOUND)
        response = super().update(request, *args, **kwargs)
        return Response({'message': UPDATE_SUCCESS.format('YouTube Link'), 'data': response.data}, status=status.HTTP_200_OK)

# Health Package Views
class HealthPackageListView(generics.ListAPIView):
    queryset = HealthPackage.objects.all()
    serializer_class = HealthPackageSerializer

class HealthPackageCreateView(generics.CreateAPIView):
    queryset = HealthPackage.objects.all()
    serializer_class = HealthPackageSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': CREATE_SUCCESS.format('Health Package'), 'data': response.data}, status=status.HTTP_201_CREATED)

class HealthPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthPackage.objects.all()
    serializer_class = HealthPackageSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            self.get_object()
        except HealthPackage.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('Health Package')}, status=status.HTTP_404_NOT_FOUND)
        super().destroy(request, *args, **kwargs)
        return Response({'message': DELETE_SUCCESS.format('Health Package')}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            self.get_object()
        except HealthPackage.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('Health Package')}, status=status.HTTP_404_NOT_FOUND)
        response = super().update(request, *args, **kwargs)
        return Response({'message': UPDATE_SUCCESS.format('Health Package'), 'data': response.data}, status=status.HTTP_200_OK)

# Health Package Booking View (Create Subscription)
class HealthPackageBookingView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        package_id = request.data.get('package_id')

        try:
            package = HealthPackage.objects.get(id=package_id)
        except HealthPackage.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('Health Package')}, status=status.HTTP_404_NOT_FOUND)

        subscription = Subscription.objects.create(user=user, package=package, end_date='2025-12-31')
        return Response({'message': CREATE_SUCCESS.format('Subscription'), 'data': SubscriptionSerializer(subscription).data}, status=status.HTTP_201_CREATED)

# Subscription Views
class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Subscription.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('Subscription')}, status=status.HTTP_404_NOT_FOUND)
        super().destroy(request, *args, **kwargs)
        return Response({'message': DELETE_SUCCESS.format('Subscription')}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Subscription.DoesNotExist:
            return Response({'error': OBJECT_NOT_FOUND.format('Subscription')}, status=status.HTTP_404_NOT_FOUND)
        response = super().update(request, *args, **kwargs)
        return Response({'message': UPDATE_SUCCESS.format('Subscription'), 'data': response.data}, status=status.HTTP_200_OK)
