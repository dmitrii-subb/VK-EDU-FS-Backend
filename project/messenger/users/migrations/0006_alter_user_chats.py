# Generated by Django 4.1.2 on 2022-10-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_alter_message_author_alter_message_chat'),
        ('users', '0005_alter_user_chats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chats',
            field=models.ManyToManyField(blank=True, to='chats.chat', verbose_name='Чаты'),
        ),
    ]
