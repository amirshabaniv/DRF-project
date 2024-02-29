from django.contrib import admin
from .models import News, NewsCategory


admin.site.register(NewsCategory)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
