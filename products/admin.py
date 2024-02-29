from django.contrib import admin
from .models import City, Province, Representation, Category, Product, CreateRepresentation

admin.site.register(City)
admin.site.register(Province)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)


@admin.register(Representation)
class RepresentationAdmin(admin.ModelAdmin):
    raw_id_fields = ('city','province')


@admin.register(CreateRepresentation)
class CreateRepresentationAdmin(admin.ModelAdmin):
    raw_id_fields = ('city','province')
