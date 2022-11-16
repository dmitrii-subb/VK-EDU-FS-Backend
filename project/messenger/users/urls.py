from django.urls import path
from users.views import (
    AddUserAsMember,
    DeleteUserFromChat,
)

urlpatterns = [
    path('user/<int:pk>/add_to_chat/<int:chat_id>/', AddUserAsMember.as_view()),
    path('user/<int:pk>/delete_from_chat/<int:chat_id>/',
         DeleteUserFromChat.as_view()),
]
