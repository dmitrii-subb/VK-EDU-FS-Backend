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
# from rest_framework.permissions import IsAuthenticated


class UserChats(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return Chat.objects.filter(author_id=user_id)


class ChatDetails(generics.RetrieveUpdateDestroyAPIView):
    ''' обрабатывает get, put, patch, delete запросы '''
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (AdminOrAuthor,)


class ChatMessages(generics.ListCreateAPIView):
    ''' обрабатывает get и post запросы '''
    serializer_class = MessageSerializer
    permission_classes = (AdminOrAuthor,)

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        return Message.objects.filter(chat_id=chat_id)


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    ''' обрабатывает get, put, patch, delete запросы '''
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (AdminOrAuthor,)
