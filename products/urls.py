from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('products', views.ProductViewSet, basename='products')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('representations', views.RepresentationViewSet, basename='representations')
router.register('create_representation', views.CreateRepresentationViewSet, basename='create_representation')


urlpatterns = [
    path('', include(router.urls)),
    path('<slug:category_name>', views.HomeAPIView.as_view(), name='home'),
]
