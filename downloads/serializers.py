from rest_framework import serializers
from .models import Download
from products.models import Category


class DownloadSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Download
        fields = ['id', 'title', 'description', 'file', 'created', 'image']


class DownloadForCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Download
        fields = ['id', 'image', 'title']


class DownloadCategorySerializer(serializers.ModelSerializer):
    downloads = DownloadForCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'downloads']
