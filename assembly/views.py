from rest_framework import mixins
from rest_framework import viewsets

from .models import BoardAssembly
from .serializers import BoardAssemblySerialzier


class BoardAssemblyViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = BoardAssemblySerialzier
    queryset = BoardAssembly.objects.all()
