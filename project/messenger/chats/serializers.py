from rest_framework import serializers
from .models import Chat, Message


# curl -X POST -d '{"title": "test chat", "description": "test chat", "author_id": 1}' 'http://127.0.0.1:8000/api/v1/chats/chats/' -H 'Content-Type: application/json'

# url -X PUT -d '{"title": "blablabla", "description": "test chat", "author_id": 1}' 'http://127.0.0.1:8000/api/v1/chats/chats/2' -H 'Content-Type: application/json'
class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        # fields = ('title', 'description', 'author_id')

    # title = serializers.CharField()
    # description = serializers.CharField(max_length = 20)
    # author_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Chat.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     # instance это объект модели Chat
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.author_id = validated_data.get('author_id', instance.author_id)
    #     instance.save()
    #     return instance



# curl -X POST -d '{"text": "test msg", "chat_id": 2, "author_id": 1}' -H 'Content-Type: application/json' 'http://127.0.0.1:8000/api/v1/chats/messages/'

# curl -X PUT -d '{"text": "blablabla", "chat_id": 2, "author_id": 1, "is_readen": true}' 'http://127.0.0.1:8000/api/v1/chats/messages/2/' -H 'Content-Type: application/json
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
    # text = serializers.CharField()
    # is_readen = serializers.BooleanField(default=False)
    # author_id = serializers.IntegerField()
    # chat_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Message.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     # instance это объект модели Chat
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.is_readen = validated_data.get('is_readen', instance.is_readen)
    #     instance.author_id = validated_data.get('author_id', instance.author_id)
    #     instance.chat_id = validated_data.get('chat_id', instance.chat_id)
    #     instance.save()
    #     return instance


