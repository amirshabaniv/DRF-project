from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('learnings', views.LearningViewSet, basename='learnings')
router.register('learning_categories', views.LearningCategoryViewSet, basename='learning_categories')
router.register('questions', views.QuestionViewSet, basename='questions')
router.register('answers', views.AnswerViewSet, basename='answers')

urlpatterns = [
    path('', include(router.urls)),
]