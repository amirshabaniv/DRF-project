from django.contrib import admin
from .models import Download, DownloadCategory


admin.site.register(DownloadCategory)


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)