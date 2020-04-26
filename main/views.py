from django.shortcuts import render, redirect, reverse
from main.models import ListModel


def main_view(request):
    user = request.user
    lists = ListModel.objects.filter(
        user=user
    ).order_by(
        'created'
    )
    context = {
        'lists': lists,
        'user': request.user.username
    }
    return render(request, 'index.html', context)


def edit_view(request, pk):
    return 'Hello'


def list_item_view(request, pk):
    pass
