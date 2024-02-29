from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('downloads', views.DownloadsViewSet, basename='downloads')
router.register('download_categories', views.DownloadCategoryViewSet, basename='download_categories')

urlpatterns = [
    path('', include(router.urls)),
]