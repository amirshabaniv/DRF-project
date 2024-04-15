from django.db import models


class DownloadCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Download Category'
        verbose_name_plural = 'Download Categories'

    def __str__(self):
        return self.name


class Download(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/download_images')
    description = models.TextField()
    file = models.FileField(upload_to='files/download_files', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(DownloadCategory, on_delete=models.CASCADE, related_name='downloads')

    def __str__(self):
        return self.title
