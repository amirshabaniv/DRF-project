from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'

    def __str__(self):
        return self.name


class News(models.Model):
    content = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/news_images')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title