from django.db import models


class Product(models.Model):
    name = models.CharField('Назва', max_length=50)
    brand = models.CharField('Бренд', max_length=50)
    description = models.TextField('Опис')
    price = models.IntegerField('Ціна')

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = 'Product'
         verbose_name_plural = 'Products'


class ProductImages(models.Model):
    image = models.ImageField(upload_to="img/products", blank=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class GlassCharacteristics(models.Model):
    SEX_CHOICES = [('M', 'Чоловічі'),('W', 'Жіночі'),('U','Унісекс')]
    FORM_CHOICES = [('С', 'Кругла'), ('N', 'Нестандартна'), ('S','Квадратна'), ('C', 'Котяче око'), ('P', 'Прямокутна')]
    COLOR_CHOICES = [('#FFFFFF', 'білий'), ('#00BFFF', 'блакитний'), ('#800000', 'бордовий'),('#FFFF00', 'жовтий'),
                     ('#008000', 'зелений'), ('#FFD700', 'золотий'), ('#8B4513', 'карі'), ('#964B00', 'коричневий'),
                     ('#FFA500', 'помаранчевий'), ('#######', 'прозорий'), ('#FFC0CB', 'рожевий'),
                     ('#808080', 'сірий'), ('#0000FF', 'синій'), ('#00008B', 'темно-синій'), ('#800080', 'фіолетовий'),
                     ('#000000', 'чорний')]
    MATERIAL_CHOICES = [('metal', 'метал'), ('titanium', 'титан'),('stainless steel', 'нержавіюча сталь'),
                        ('plastic', 'пластик'), ('wood', 'дерево')]

    gender = models.CharField('Стать', max_length=1, choices=SEX_CHOICES)
    glass_form = models.CharField('Форма окулярів', max_length=1, choices=FORM_CHOICES)
    glass_color = models.CharField('Колір окулярів', max_length=7, choices=COLOR_CHOICES)
    lens_color = models.CharField('Колір лінз', max_length=7, choices=COLOR_CHOICES)
    glass_material = models.CharField('Матеріал оправи', max_length=15, choices=MATERIAL_CHOICES)
    size_eyepiece = models.PositiveIntegerField('Розмір окуляра')
    size_earring = models.PositiveIntegerField('Розмір завушника')
    size_bridge = models.PositiveIntegerField('Розмір мостика')
    product = models.OneToOneField(Product, related_name='characteristics', on_delete=models.CASCADE)
