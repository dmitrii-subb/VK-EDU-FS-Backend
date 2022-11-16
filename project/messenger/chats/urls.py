from django.urls import path
from chats.views import (
    UserChats,
    ChatMessages,
    ChatDetails,
    MessageDetails,
)

urlpatterns = [
    path('owned_by_user/<int:pk>/', UserChats.as_view()),
    path('messages_in_chat/<int:chat_id>/', ChatMessages.as_view()),
    path('chat_details/<int:pk>/', ChatDetails.as_view()),
    path('message_details/<int:pk>/', MessageDetails.as_view()),
]
