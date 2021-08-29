from django.db import models
from django.urls import reverse


# это для моделей которые используются в бд
class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')  # для текста
    content = models.TextField(blank=True, verbose_name='Контент')
    created_add = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')  # формат даты и когда добавил
    update_add = models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото',
                              blank=True)  # для изображений и куда когда и во сколько было создано
    is_published = models.BooleanField(default=True,
                                       verbose_name='На сайте')  # для неопубликованных новость по умолчанию публикуется
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_add']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
