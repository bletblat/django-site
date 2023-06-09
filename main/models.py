from django.db import models
from mptt.models import TreeForeignKey, MPTTModel


class MenuItem(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField('Ссылка', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=1)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class Tabbs(models.Model):
    tabb_name = models.CharField('Название', max_length=100)
    tabb_text = models.TextField('Текст', max_length=500, default="Какой-то текст")

    def __str__(self):
        return self.tabb_name

# class TabbItem(MPTTModel):
#     name = models.CharField(max_length=100, unique=True)
#     position = models.PositiveIntegerField('Позиция', default=1)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

#     class MPTTMeta:
#         order_insertion_by = ['position']

#     def __str__(self):
#         return str(self.name)

#     class Meta:
#         verbose_name = 'Таб'
#         verbose_name_plural = 'Табы'