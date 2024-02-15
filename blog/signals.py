from .models import PostModel
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .task import send_message_to_telegram_channel as send_post_task, send_delete_post
from asyncio import run
from telegrambot.models import TelegramBot


@receiver(post_save, sender=PostModel)
def send_post_to_telegram_channel(sender, instance, created, **kwargs):
    if created:
        author = instance.author
        chat_id = None
        token = None
        if TelegramBot.objects.filter(username=author).exists():
            tg_config = TelegramBot.objects.get(username=author)
            chat_id = tg_config.chat_id
            token = tg_config.token
        
        
        post_data = {
            'token': token,
            'chat_id': chat_id,
            'title': instance.title,
            'url_address': instance.get_absolute_url(),
        }
        run(send_post_task(post_data))


@receiver(post_delete, sender=PostModel)
def delete_post(sender, instance, **kwargs):
    print(f'[*]{instance.id}  Post {instance.title} deleted from DB')
    author = instance.author
    chat_id = None
    token = None
    if TelegramBot.objects.filter(username=author).exists():
        tg_config = TelegramBot.objects.get(username=author)
        chat_id = tg_config.chat_id
        token = tg_config.token
    
    post_data = {
        'token': token,
        'chat_id': chat_id,
        'title': instance.title,
        'url_address': instance.get_absolute_url(),
    }
    run(send_delete_post(post_data))
    