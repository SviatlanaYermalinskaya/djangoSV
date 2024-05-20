from django.core.validators import RegexValidator
from django.db import models

from users.models import CustomUser


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=52, verbose_name='Название')
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='URL slug')

    def __str__(self):
        return self.title


class Product(models.Model):
    GENDER_CHOICES = (
        ('М', 'Мужское'),
        ('Ж', 'Женское'),
    )

    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'ExtraLarge'),
    )
    title = models.CharField(max_length=56, verbose_name='Название')
    price = models.FloatField(default=0, verbose_name='Цена')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SIZE_CHOICES[0][0], verbose_name='Размер')
    quantity = models.IntegerField(default=0, verbose_name='Количество товара')
    product_description = models.TextField('Описание товара')
    model_description = models.TextField(verbose_name='Описание модели')
    delivery_description = models.TextField(verbose_name='Описание доставки')
    vendor_code = models.CharField(max_length=52, verbose_name='Артикул')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0], verbose_name='Пол')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


class Order(models.Model):
    STATUS_CHOICES = (
        ('Вп', 'В процессе'),
        ('О', 'Оплачен'),
        ('С', 'Собирается'),
        ('От', 'Отправлен'),
        ('В', 'В пути'),
        ('Ж', 'Ждет получения'),
        ('П', 'Получен'),
    )
    products = models.ManyToManyField(Product, verbose_name='Товары')
    name = models.CharField(max_length=52, verbose_name='Имя', blank=True, null=True)
    surname = models.CharField(max_length=52, verbose_name='Фамилия', blank=True, null=True)
    patronymic = models.CharField(max_length=52, verbose_name='Отчество', blank=True, null=True)
    email = models.EmailField(verbose_name='Email')
    phoneNumberRegex = RegexValidator(regex=r'^((\+\d{,4})[\- ]?)?(\(?\d{2,3}\)?[\- ]?)?[\d\- ]{7,10}$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    region = models.CharField(max_length=52, verbose_name='Область', blank=True, null=True)
    city = models.CharField(max_length=52, verbose_name='Город', blank=True, null=True)
    street_name = models.CharField(max_length=52, verbose_name='Название улицы', blank=True, null=True)
    house_number = models.IntegerField(verbose_name='Номер дома', blank=True, null=True)
    entrance = models.IntegerField(verbose_name='Подъезд', blank=True, null=True)
    floor = models.IntegerField(verbose_name='Этаж', blank=True, null=True)
    apartment = models.IntegerField(verbose_name='Номер квартиры', blank=True, null=True)
    post_code = models.IntegerField(verbose_name='Почтовый индекс', blank=True, null=True)
    comment = models.TextField(max_length=300, verbose_name='Комментарий', blank=True, null=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Заказчик')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Статус')

    def __str__(self):
        return f'{self.name} {self.surname}'






















