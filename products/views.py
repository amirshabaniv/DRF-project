from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Product, Category, Representation, CreateRepresentation
from .serializers import ProductSerializer, CategorySeializer, RepresentationSerializer, CreateRepresentationSerializer
from rest_framework.decorators import action
from django.core.cache import cache
from news.models import News
from news.serializers import NewsSerializer


from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin

class HomeViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        latest_category1_products = self.queryset.filter(category__name='category1').order_by('-created')[:3]
        latest_category2_products = self.queryset.filter(category__name='category2').order_by('-created')[:3]
        latest_news = News.objects.all().order_by('-created')[:3]

        serializer_category1 = self.get_serializer(latest_category1_products, many=True)
        serializer_category2 = self.get_serializer(latest_category2_products, many=True)
        serializer_news = NewsSerializer(latest_news, many=True)

        data = {
            'latest_category1_products': serializer_category1.data,
            'latest_category2_products': serializer_category2.data,
            'latest_news': serializer_news.data
        }

        return Response(data)
    

class ProductViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    @action(detail=True, methods=['get'])
    def add_view(self, request, *args, **kwargs):
        instance = self.get_object()
        
        cache_key = f'product_{instance.id}_views'
        views = cache.get(cache_key, 0) + 1
        cache.set(cache_key, views)

        instance.views_count = views
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CategorySeializer
    queryset = Category.objects.all()


class RepresentationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = RepresentationSerializer
    queryset = Representation.objects.all()


class CreateRepresentationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateRepresentationSerializer
    queryset = CreateRepresentation.objects.all()


