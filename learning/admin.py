from django.contrib import admin
from .models import LearningCategory, Learning


admin.site.register(LearningCategory)

@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)