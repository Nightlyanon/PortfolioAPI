from photos.models import Photo
from rest_framework import viewsets, permissions
from .serializers import PhotoSerializer

#Photo Viewset
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [
            permissions.AllowAny
    ]
