from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL категории")
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Родительская категория"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class MPTTMeta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']  # Для сортировки категорий по имени

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category_detail', kwargs={'slug': self.slug})


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', verbose_name="Пользователь")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Поле для загрузки изображений
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Широта
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Долгота

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
    def __str__(self):
        return self.title
    

class CategoryFeature(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=100)  # Название характеристики
    value = models.TextField(blank=True, null=True)  # Значение характеристики

    def __str__(self):
        return f"{self.name}: {self.value} (Category: {self.category.name})"
    