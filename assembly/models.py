from django.db import models


class BoardAssembly(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    file = models.FileField(upload_to='files/assembly_files', null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Board Assembly'
        verbose_name_plural = 'Board Assemblies'

    def __str__(self):
        return f'{self.name} requested assembly board'