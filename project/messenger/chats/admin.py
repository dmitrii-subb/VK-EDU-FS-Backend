from django.contrib import admin

# Register your models here.
from chats.models import Chat, Message


class ChatAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'id']
    raw_id_fields = ['author']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'id', 'chat']
    raw_id_fields = ['author', 'chat']


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
