from django.shortcuts import render, redirect, reverse
from main.models import ListModel
from main.forms import ListForm


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


def new_list_view(request):
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(data=request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'new_list.html', {'form': form})
