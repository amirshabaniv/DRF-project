from django.db import models
from accounts.models import UserModel


class LearningCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Leraning Category'
        verbose_name_plural = 'Learning Categories'

    def __str__(self):
        return self.name

class Learning(models.Model):
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/learning_images')
    file = models.FileField(upload_to='files/learning_files')
    video = models.FileField(upload_to='files/learning_videos', null=True, blank=True)
    category = models.ForeignKey(LearningCategory, on_delete=models.CASCADE, related_name='learnings')

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()

    def __str__(self):
        return self.question.title