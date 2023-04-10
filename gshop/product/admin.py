from django.contrib import admin
from .models import Product, ProductImages, GlassCharacteristics


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1


class GlassCharacteristicsInline(admin.StackedInline):
    model = GlassCharacteristics


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline, GlassCharacteristicsInline]


admin.site.register(Product, ProductAdmin)
