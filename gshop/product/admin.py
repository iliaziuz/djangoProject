from django.contrib import admin
from .models import Product, ProductImages


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1  # кількість додаткових полів для завантаження зображень


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]


admin.site.register(Product, ProductAdmin)