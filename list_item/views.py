from django.shortcuts import render
from list_item.models import ListItemModel
from main.models import ListModel


def list_item_view(request, pk):
    lists = ListItemModel.objects.filter(listmodel=pk).order_by(
        'priority')
    title = ListModel.objects.filter(id=pk).first()

    context = {
        'lists': lists,
        'user': request.user.username,
        'title': title

    }
    return render(request, 'list.html', context)
