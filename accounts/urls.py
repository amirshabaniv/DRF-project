from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('profile', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]