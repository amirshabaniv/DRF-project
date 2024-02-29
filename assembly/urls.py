from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('AssemblyRequest', views.BoardAssemblyViewSet, basename='boardassembly')

urlpatterns = [
    path('', include(router.urls)),
]