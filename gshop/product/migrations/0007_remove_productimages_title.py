# Generated by Django 4.1.7 on 2023-04-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_picture_productimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='title',
        ),
    ]