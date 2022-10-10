from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def all_chats(request):
    return JsonResponse({'chats': []})


@require_http_methods(['GET'])
def chat_page(request, chat_id):
    return JsonResponse({'chat_id': chat_id})


@require_http_methods(['POST'])
def create_chat(request):
    return JsonResponse({'create': True})
