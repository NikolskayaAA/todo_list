from django.shortcuts import render

# Create your views here.
data = {
    'lists': [
        {'name': 'Купить шариков', 'is_done': True, 'date': False},
        {'name': 'Заказать торт', 'is_done': True, 'date': '05.06.20'},
        {'name': 'Разослать приглашения', 'is_done': False, 'date': False}
    ],
    'user_name': 'Admin',
}


def list_item_view(request):
    context = data
    return render(request, 'list.html', context)
