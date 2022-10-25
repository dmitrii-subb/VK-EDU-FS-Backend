import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from chats.models import Message, Chat
from users.models import User
from django.core.exceptions import ObjectDoesNotExist


def parse_request(request):
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return {
            'ok': False,
            'result': 'wrong json format'
        }
    return {
        'ok': True,
        'data': data
    }


# curl -X PUT -d '{"chat_id": 1, "title": "dmitrii oreshkin", "description": "test chat", "author_id": 1}' 'http://127.0.0.1:8000/chats/update_chat/'
@require_http_methods(['PUT'])
def update_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data.get('chat_id')
    try:
        chat = Chat.objects.get(id=chat_id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'chat with id={chat_id} does not exists'
        })
    title = data.get('title')
    description = data.get('description')
    author_id = data.get('author_id')

    if title is not None:
        chat.title = title

    if description is not None:
        chat.description = description

    if author_id is not None:
        try:
            author = User.objects.get(id=author_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'ok': False,
                'result': f'user with id={author_id} does not exists'
            })
        chat.author = author

    chat.save()
    return JsonResponse({
        'ok': True
    })


# curl -X PUT -d '{"message_id": 1, "text": "dmitrii oreshkin", "author_id": 1}' 'http://127.0.0.1:8000/chats/update_message/'
@require_http_methods(['PUT'])
def update_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    message_id = data.get('message_id')
    try:
        message = Message.objects.get(id=message_id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'message with id={message_id} does not exists'
        })
    text = data.get('text')
    author_id = data.get('author_id')

    if author_id is not None:
        try:
            author = User.objects.get(id=author_id)
        except ObjectDoesNotExist:
            return JsonResponse({
                'ok': False,
                'result': f'user with id={author_id} does not exists'
            })

        if message.author != author:
            return JsonResponse({
                'ok': False,
                'result': f'message with id={message_id} is not owned by user with id={author.id}'
            })
        if text is not None:
            message.text = text

        message.save()

    return JsonResponse({
        'ok': True
    })


#  curl -X GET -d '{"chat_id": 1}' 'http://127.0.0.1:8000/chats/get_all_messages/'
@require_http_methods(['GET'])
def get_all_messages(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data['chat_id']
    try:
        chat = Chat.objects.get(id=chat_id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'chat with id={chat_id} does not exists'
        })
    try:
        messages = Message.objects.filter(chat=chat)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'no messages in chat id={chat.id}'
        })
    response = {}
    for message in messages:
        response[message.id] = {
            'text': message.text,
            'date': message.date,
            'author_id': message.author.id
        }

    return JsonResponse({'ok': True, 'result': response})


# curl -X GET -d '{"user_id": 1}' 'http://127.0.0.1:8000/chats/get_all_chats/'
@require_http_methods(['GET'])
def get_all_chats(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    user_id = data['user_id']
    try:
        author = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'user with id={user_id} does not exists'
        })
    try:
        chats = Chat.objects.filter(author=author)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'no chats where author is {author.username}'
        })
    response = {}
    for chat in chats:
        response[chat.id] = {
            'title': chat.title,
            'description': chat.description,
            'author_id': chat.author.id
        }

    return JsonResponse({'ok': True, 'result': response})


# curl -X GET -d '{"chat_id": 1}' 'http://127.0.0.1:8000/chats/get_chat/'
@require_http_methods(['GET'])
def get_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data.get('chat_id')
    try:
        chat = Chat.objects.get(id=chat_id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'chat with id={chat_id} does not exists'
        })

    return JsonResponse({
        'ok': True,
        'result': {
            'id': chat.id,
            'title': chat.title,
            'description': chat.description,
            'author_id': chat.author.id
        }
    })


# curl -X GET -d '{"message_id": 1}' 'http://127.0.0.1:8000/chats/get_message/'
@require_http_methods(['GET'])
def get_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    message_id = data.get('message_id')
    try:
        message = Message.objects.get(id=message_id)
    except ObjectDoesNotExist:
        return JsonResponse({
            'ok': False,
            'result': f'message with id={message_id} does not exists'
        })

    return JsonResponse({
        'ok': True,
        'result': {
            'id': message.id,
            'text': message.text,
            'date': message.date,
            'author_id': message.author.id,
            'chat_id': message.chat.id
        }
    })


# curl -d '{"title": "dmitrii oreshkin", "description": "test chat", "author": "dmitrii"}' 'http://127.0.0.1:8000/chats/create_chat/'
@require_http_methods(['POST'])
def create_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    title = data.get('title')
    description = data.get('description')
    username = data.get('author')
    try:
        author = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'ok': False, 'result': f'user {username} does not exists'})

    Chat.objects.create(title=title, description=description, author=author)
    return JsonResponse({'ok': True})


# curl -d '{"chat_id": 2}' 'http://127.0.0.1:8000/chats/delete_chat/'
@require_http_methods(['POST'])
def delete_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data.get('chat_id')
    try:
        Chat.objects.get(id=chat_id).delete()
    except ObjectDoesNotExist:
        return JsonResponse({'ok': False, 'result': f'chat with id={chat_id} does not exists'})

    return JsonResponse({'ok': True})


# curl -d '{"text": "test message", "author": "dmitrii", "chat_id": 1}' 'http://127.0.0.1:8000/chats/create_message/'
@require_http_methods(['POST'])
def create_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    text = data.get('text')
    username = data.get('author')
    chat_id = data.get('chat_id')
    try:
        author = User.objects.get(username=username)
    except ObjectDoesNotExist:
        return JsonResponse({'ok': False, 'result': f'user {username} does not exists'})

    try:
        chat = Chat.objects.get(id=chat_id)
    except ObjectDoesNotExist:
        return JsonResponse({'ok': False, 'result': f'chat with id={chat_id} does not exists'})

    Message.objects.create(text=text, author=author, chat=chat)
    return JsonResponse({'ok': True})


# curl -d '{"message_id": 1}' 'http://127.0.0.1:8000/chats/delete_message/'
@require_http_methods(['POST'])
def delete_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    message_id = data.get('message_id')
    try:
        Message.objects.get(id=message_id).delete()
    except ObjectDoesNotExist:
        return JsonResponse({'ok': False, 'result': f'message with id={message_id} does not exists'})

    return JsonResponse({'ok': True})
