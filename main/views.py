from django.shortcuts import render

# Create your views here.

data = {
    'lists': [
        {'id': 1, 'name': 'Работа', 'is_done': True},
        {'id': 2, 'name': 'Дом', 'is_done': True},
        {'id': 3, 'name': 'Учеба', 'is_done': False}
    ],
    'user_name': 'Admin',
}


def main_view(request, pk):
    context = data
    return render(request, 'index.html', context)


def edit_view(request, pk):
    return 'Hello'
