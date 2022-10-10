from django.urls import path
from chats.views import all_chats, chat_page, create_chat


urlpatterns = [
    path('', all_chats, name='all_chats'),
    path('<int:chat_id>/', chat_page, name='chat_page'),
    path('new/', create_chat, name='create_chat')
]
