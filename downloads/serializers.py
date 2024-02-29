from rest_framework import serializers
from .models import Download, DownloadCategory


class DownloadSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Download
        fields = ['id', 'title', 'description', 'file', 'created', 'image']


class DownloadForCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Download
        fields = ['id', 'image', 'title']


class DownloadCategorySerializer(serializers.ModelSerializer):
    news = DownloadForCategorySerializer(many=True)

    class Meta:
        model = DownloadCategory
        fields = ['id', 'name', 'downloads']