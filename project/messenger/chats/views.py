from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Chat, Message
from users.models import User
from .serializers import ChatSerializer, MessageSerializer
from users.serializers import UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


# curl -X GET -d '{"user_id": 2}' 'http://127.0.0.1:8000/api/v1/chats/chats/' -H 'Content-Type: application/json'
class ChatsAPIList(generics.ListCreateAPIView):
    ''' обрабатывает get и post запросы
        создание чата, список всех чатов пользователя
    '''
    # queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        # user_id = self.request.data.get('user_id')
        # print(self.request.data)
        # print(self.kwargs)
        user_id = self.kwargs.get('user_id')
        return Chat.objects.filter(author_id=user_id)

class ChatsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#   обрабатывает get, put, patch, delete запросы
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


# curl -X GET -d '{"chat_id": 2}' 'http://127.0.0.1:8000/api/v1/chats/messages/' -H 'Content-Type: application/json'
class MessagesAPIList(generics.ListCreateAPIView):
#   обрабатывает get и post запросы
    serializer_class = MessageSerializer

    def get_queryset(self):
        # chat_id = self.request.data.get('chat_id')
        # print(self.request.data)
        chat_id = self.kwargs.get('chat_id')
        print(chat_id)
        return Message.objects.filter(chat_id=chat_id)

class MessagesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#   обрабатывает get, put, patch, delete запросы
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


# curl -d '{"chat_id": 1, "user_id": 1}' 'http://127.0.0.1:8000/api/v1/chats/chat/delete_member/'
class DeleteMemberFromChat(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.request.data.get('user_id')
        chat_id = self.request.data.get('chat_id')
        chat = Chat.objects.get(id=chat_id)
        user = User.objects.get(id=user_id)
        # print(self.request.data)
        user.chats.remove(chat)
        user.save()
        return {'ok': True}



# class ChatsAPIView(APIView):
#     def get(self, request):
#         qs = Chat.objects.all()
#         return Response({'get' : ChatSerializer(qs, many=True).data})
#
#     def post(self, request):
#         serializer = ChatSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'not allowed'})
#
#         try:
#             instance = Chat.objects.get(pk=pk)
#         except:
#             return Response({'error': 'object does not exist'})
#
#         serializer = ChatSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'put': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'delete not allowed'})
#
#         try:
#             instance = Message.objects.get(pk=pk)
#         except:
#             return Response({'error': 'object does not exist'})
#
#         Message.objects.get(pk=pk).delete()
#         return Response({'delete': True})
#
# class MessagesAPIView(APIView):
#     def get(self, request):
#         qs = Message.objects.all()
#         return Response({'get' : MessageSerializer(qs, many=True).data})
#
#     def post(self, request):
#         serializer = MessageSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'put not allowed'})
#
#         try:
#             instance = Message.objects.get(pk=pk)
#         except:
#             return Response({'error': 'object does not exist'})
#
#         serializer = MessageSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'put': serializer.data})
#
#     # curl -X DELETE 'http://127.0.0.1:8000/api/v1/chats/messages/5/' -H 'Content-Type: application/json'
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if not pk:
#             return Response({'error': 'delete not allowed'})
#
#         try:
#             instance = Message.objects.get(pk=pk)
#         except:
#             return Response({'error': 'object does not exist'})
#
#         Message.objects.get(pk=pk).delete()
#         return Response({'delete': True})

