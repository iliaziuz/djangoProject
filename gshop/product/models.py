from django.db import models


class Product(models.Model):
    name = models.CharField('Назва', max_length=50)
    brand = models.CharField('Бренд', max_length=50)
    description = models.TextField('Опис')
    price = models.IntegerField('Ціна')

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = 'Товар'
         verbose_name_plural = 'Товари'


class ProductImages(models.Model):
    image = models.ImageField(upload_to="img/products", blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class GlassCharacteristics(models.Model):
    SEX_CHOICES = [('Чоловічі', 'Чоловічі'),('Жіночі', 'Жіночі'),('Унісекс','Унісекс'),('Дитячі','Дитячі')]
    FORM_CHOICES = [('Кругла', 'Кругла'), ('Нестандартна', 'Нестандартна'), ('Квадратна','Квадратна'),
                    ('Котяче око', 'Котяче око'), ('Прямокутна', 'Прямокутна')]
    COLOR_CHOICES = [('Білий', 'Білий'), ('Блакитний', 'Блакитний'), ('Бордовий', 'Бордовий'),('Жовтий', 'Жовтий'),
                     ('Зелений', 'Зелений'), ('Золотий', 'Золотий'), ('Коричневий', 'Коричневий'),
                     ('Помаранчевий', 'Помаранчевий'), ('Прозорий', 'Прозорий'), ('Рожевий', 'Рожевий'),
                     ('Сірий', 'Сірий'), ('Синій', 'Синій'), ('Срібний', 'Срібний'), ('Темно-синій', 'Темно-синій'),
                     ('Фіолетовий', 'Фіолетовий'), ('Чорний', 'Чорний')]
    MATERIAL_CHOICES = [('Метал', 'Метал'), ('Титан', 'Титан'), ('Нержавіюча сталь', 'Нержавіюча сталь'),
                        ('Пластик', 'Пластик'), ('Дерево', 'Дерево')]
    CATEGORY_CHOICES = [('Сонцезахисні окуляри', 'Сонцезахисні окуляри'), ('Оправи', 'Оправи')]

    category = models.CharField('Категорія', max_length=20, choices=CATEGORY_CHOICES, blank=True)
    gender = models.CharField('Стать', max_length=10, choices=SEX_CHOICES)
    glass_form = models.CharField('Форма окулярів', max_length=15, choices=FORM_CHOICES)
    glass_color = models.CharField('Колір окулярів', max_length=20, choices=COLOR_CHOICES)
    lens_color = models.CharField('Колір лінз', max_length=15, choices=COLOR_CHOICES, blank=True, null=True)
    glass_material = models.CharField('Матеріал оправи', max_length=20, choices=MATERIAL_CHOICES)
    size_eyepiece = models.PositiveIntegerField('Розмір окуляра', blank=True)
    size_earring = models.PositiveIntegerField('Розмір завушника', blank=True)
    size_bridge = models.PositiveIntegerField('Розмір мостика', blank=True)
    product = models.OneToOneField(Product, related_name='characteristics', on_delete=models.CASCADE)


'''
class LensCharacteristics(models.Model):
    CATEGORY_CHOICES = [('Для далі (+ або -)', 'Для далі (+ або -)'), ('Торичні', 'Торичні'),
                        ('Мультифокальні', 'Мультифокальні'), ('Кольорові', 'Кольорові'),
                        ('', ''), ('', '')]
    REPLACEMENT_MODE_CHOICES = [('1 день', '1 день'), ('2 тижні', '2 тижні'), ('1 місяць', '1 місяць'),
                                ('3 місяці', '3 місяці'), ('6 місяці', '6 місяці'), ('9 місяці', '9 місяці'),
                                ('12 місяці', '12 місяці')]

    category = models.CharField('Категорія', max_length=20, choices=CATEGORY_CHOICES)
    replacement_mode = models.CharField('Режим заміни', max_length=20, choices=REPLACEMENT_MODE_CHOICES)
    product = models.OneToOneField(Product, related_name='characteristics', on_delete=models.CASCADE)
'''