# Generated by Django 4.1.2 on 2022-10-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_alter_message_author_alter_message_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_readen',
            field=models.BooleanField(default=False),
        ),
    ]
