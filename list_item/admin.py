from django.contrib import admin
from list_item.models import ListItemModel


# Register your models here.
class ListItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'listmodel']
    list_filter = ['id', 'created', 'name', 'is_done']
    search_fields = ['name', 'listmodel']


admin.site.register(ListItemModel, ListItemAdmin)
