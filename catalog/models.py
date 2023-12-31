from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Модель, описывающая категорию товара"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    """Модель описывающая товар"""
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_date = models.DateField(verbose_name='Дата создания')
    changed_date = models.DateField(verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='признак активности товара')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    def toggle_is_published(self):
        self.is_published = not self.is_published
        self.save()
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)

        permissions = [
            (
                'set_published_product',
                'Can publish product'
            ),
            (
                'can_edit_description_and_category_product',
                'Can edit description and category product'
            )
        ]
class Contact(models.Model):
    """Модель описывающая пользователя"""
    name = models.CharField(max_length=150, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Сообщение')
    def __str__(self):
        return f'{self.name} - {self.phone}'
    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name',)


class Version(models.Model):
    """Модель, описывающая версию товара"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    num_of_version = models.CharField(default=1, verbose_name='Номер версии')
    title = models.CharField(max_length=150, verbose_name='Название версии', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='признак текущей версии')
    def __str__(self):
        return f'{self.title} - {self.num_of_version} ({self.product})'
    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'