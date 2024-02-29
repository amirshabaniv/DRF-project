from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts import views

router = DefaultRouter()
router.register("user", views.UserViewSet, basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', include('accounts.urls')),
    path('', include('products.urls')),
    path('', include('learning.urls')),
    path('', include('news.urls')),
    path('', include('assembly.urls')),
    path('', include('downloads.urls')),
]

urlpatterns += router.urls