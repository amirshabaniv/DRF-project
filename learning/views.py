from rest_framework import viewsets
from rest_framework import mixins

from .models import Learning, LearningCategory, Question, Answer
from .serializers import LearningSerializer, LearningCategorySerializer, QuestionSerializer, AnswerSerializer

from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class LearningViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = LearningSerializer
    queryset = Learning.objects.all()


class LearningCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = LearningCategorySerializer
    queryset = LearningCategory.objects.all()


class QuestionViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user)


class AnswerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    def perform_create(self, serializer):
        question_id = self.request.data.get('question')
        question = Question.objects.get(id=question_id)
        user = User.objects.get(id=self.request.user.id)
        serializer.save(user=user, question=question)
