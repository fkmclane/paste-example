from datetime import timedelta

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.http import HttpResponse

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from .models import Paste


def index(request):
    link = None

    if 'code' in request.POST:
        data = {}

        name = request.POST['name']
        if name:
            data['name'] = name

        language = request.POST['language']
        if language:
            data['language'] = language

        try:
            days = int(request.POST['expires'])
        except ValueError:
            days = 7

        data['expires'] = timezone.now() + timedelta(days=days)

        data['code'] = request.POST['code']

        paste = Paste(**data)
        paste.save()

        link = request.scheme + '://' + request.META['HTTP_HOST'] + request.path + str(paste.id)

    context = {
        'link': link,
    }

    return render(request, 'index.html', context)


def latest(request):
    latest = Paste.objects.order_by('-date')[:20]

    context = {
        'latest': latest,
    }

    return render(request, 'latest.html', context)


def prune(request):
    deletions = []

    for paste in Paste.objects.all():
        if paste.should_prune():
            deletions.append(paste)

    for paste in deletions:
        paste.delete()

    return HttpResponse('Pruned')


def paste(request, paste_id):
    paste = get_object_or_404(Paste, id=paste_id)

    try:
        lexer = get_lexer_by_name(paste.language, stripall=True)
        formatter = HtmlFormatter(linenos=True)

        highlighted = highlight(paste.code, lexer, formatter)
    except:
        highlighted = paste.code

    context = {
        'pygments': HtmlFormatter().get_style_defs('.highlight'),
        'date': paste.date,
        'name': paste.name,
        'language': paste.language,
        'expires': paste.expires,
        'code': mark_safe(highlighted),
    }

    return render(request, 'paste.html', context)
