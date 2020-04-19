from django.shortcuts import render

# Create your views here.

data = {
    'lists': [
        {'name': 'Работа', 'is_done': True},
        {'name': 'Дом', 'is_done': True},
        {'name': 'Учеба', 'is_done':False}
    ],
    'user_name': 'Admin',
}


def main_view(request):
    context = data
    return render(request, 'index.html', context)
