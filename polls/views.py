from polls.models import Makale, choice

from django.shortcuts import render


def index(request):
    context = {
        'makale': Makale.objects.all(),
        'title': 'Items',
        'choices': choice,
    }
    return render(request, 'polls/index.html', context)
