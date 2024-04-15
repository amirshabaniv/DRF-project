from rest_framework import viewsets
from rest_framework import mixins

from .models import News, NewsCategory
from .serializers import NewsSerializer, NewsCategorySerializer


class NewsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.objects.all()
