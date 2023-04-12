from django.shortcuts import render
from product.models import Product, GlassCharacteristics, ProductImages


category_map = {'sunglasses': 'Сонцезахисні окуляри',
                'eyeglasses': 'Оправи'
                }

filter_dict = {'Стать': [choice[0] for choice in GlassCharacteristics.SEX_CHOICES],
               'Категорія': [choice[0] for choice in GlassCharacteristics.CATEGORY_CHOICES],
               'Форма окулярів': [choice[0] for choice in GlassCharacteristics.FORM_CHOICES],
               'Колір окулярів': [choice[0] for choice in GlassCharacteristics.COLOR_CHOICES],
               'Колір лінз': [choice[0] for choice in GlassCharacteristics.COLOR_CHOICES],
               'Матеріал оправи': [choice[0] for choice in GlassCharacteristics.MATERIAL_CHOICES],
               }


def catalog_by_category(request, category):
    characteristics = GlassCharacteristics.objects.filter(category=category_map.get(category))
    products = [characteristic.product for characteristic in characteristics]
    context = {'products': products,
               'filter_dict': filter_dict}
    return render(request, 'catalog/catalog.html', context)


def catalog_by_brand(request, category, brand):
    products = Product.objects.filter(category=category, brand=brand)
    context = {'products': products}
    return render(request, 'catalog/catalog.html', context)


def catalog_by_sex(request, category, sex):
    products = Product.objects.filter(category=category, sex=sex)
    context = {'products': products}
    return render(request, 'catalog/catalog.html', context)
