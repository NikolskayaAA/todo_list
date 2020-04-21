from django.db import models


# Create your models here.
class ListItemModel(models.Model):
    """Модель списка дел"""
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    listmodel = models.ForeignKey('main.ListModel', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #    return self.name

    class Meta:
        verbose_name = 'День рождения'
