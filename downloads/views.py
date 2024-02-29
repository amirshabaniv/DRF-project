from rest_framework import mixins
from rest_framework import viewsets

from .models import Download, DownloadCategory
from .serializers import DownloadSerialzier, DownloadCategorySerializer


class DownloadsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DownloadSerialzier
    queryset = Download.objects.all()


class DownloadCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = DownloadCategorySerializer
    queryset = DownloadCategory.objects.all()