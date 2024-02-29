from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('news', views.NewsViewSet, basename='news')
router.register('news_categories', views.NewsCategoryViewSet, basename='news_categories')

urlpatterns = [
    path('', include(router.urls)),
]