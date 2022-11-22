from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from users.models import User
from users.serializers import UserSerializer

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from .permissions import AdminOrAuthor
from .utils import publish_message


class UserChats(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        user_id = self.request.user.id  # неавторизованный не пройдет
        print(user_id)
        return Chat.objects.filter(author_id=user_id)


class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
    ''' обрабатывает get, put, patch, delete запросы '''
    serializer_class = ChatSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        user_id = self.request.user.id  # неавторизованный не пройдет
        chat_id = self.kwargs.get('pk')
        return Chat.objects.filter(Q(author_id=user_id) & Q(id=chat_id))


class ChatMessages(generics.ListCreateAPIView):
    ''' обрабатывает get и post запросы '''
    serializer_class = MessageSerializer
    # permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat_id=chat_id)

    def create(self, request, *args, **kwargs):
        # message = self.get_object()
        text = request.data.get('text')
        chat_id = request.data.get('chat_id')
        print(f'msg: {text} | from id: {chat_id}')
        # Message.objects.create(text=text)
        publish_message({'msg': text, 'chat_id': chat_id})
        return Response({})


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    ''' обрабатывает get, put, patch, delete запросы '''
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AdminOrAuthor,)
