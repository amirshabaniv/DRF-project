from rest_framework import serializers
from .models import Learning, LearningCategory, Question, Answer


class LearningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Learning
        fields = ['id', 'description', 'title', 'image',
                  'file', 'video', 'category']


class LearningForCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Learning
        fields = ['id', 'image', 'title']


class LearningCategorySerializer(serializers.ModelSerializer):
    learnings = LearningForCategorySerializer(many=True)

    class Meta:
        model = LearningCategory
        fields = ['id', 'name', 'learnings']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'user', 'text', 'answers']