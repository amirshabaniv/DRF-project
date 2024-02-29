from rest_framework import serializers
from .models import News, NewsCategory


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'content', 'title', 'image', 'category', 'created']


class NewsForCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'image', 'title']


class NewsCategorySerializer(serializers.ModelSerializer):
    news = NewsForCategorySerializer(many=True)

    class Meta:
        model = NewsCategory
        fields = ['id', 'name', 'news']