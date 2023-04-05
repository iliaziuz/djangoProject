# Generated by Django 4.1.7 on 2023-04-04 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='img/poster')),
            ],
            options={
                'verbose_name': 'Poster',
                'verbose_name_plural': 'Posters',
            },
        ),
        migrations.DeleteModel(
            name='Pictures',
        ),
    ]