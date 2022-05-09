from polls.models import Makale, Slide, choice

from django.shortcuts import render, get_object_or_404


def index(request):
    context = {
        'makale': Makale.objects.all(),
        'title': 'Items',
        'choices': choice,
        'slide': Slide.objects.all()
    }
    return render(request, 'polls/index.html', context)


def article(request, slug):
    makale = get_object_or_404(Makale, slug=slug)
    context = {
        'icerik': Makale.objects.all(),
        "makale": makale
    }
    return render(request, 'polls/article.html', context)
