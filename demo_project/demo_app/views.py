from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse


@require_http_methods(['GET'])
def index(request):
    return HttpResponse('Hello world!')