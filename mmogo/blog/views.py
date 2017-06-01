from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext


def index(request):
    context = RequestContext(request, {})
    return render(
        request, 'app/index.html', context)
