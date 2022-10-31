from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def index(request):
    return render(request, 'start/index.html')
