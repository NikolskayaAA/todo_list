from django.db import models


# Create your models here.
class ListItemModel(models.Model):
    """Модель элемента Работа'"""
    name = models.CharField(max_length=128, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    listmodel = models.ForeignKey('main.ListModel', on_delete=models.CASCADE, verbose_name='Список дел')
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(blank=True, null=True)
    priority = models.SmallIntegerField(verbose_name='Приоритет', default=0)

    # def __str__(self):
    #    return self.name

    class Meta:
        verbose_name = 'Элемент списка'
