from .models import PostModel
from django.dispatch import receiver
from django.db.models.signals import post_save
from .task import send_message_to_telegram_channel as send_post_task
from asgiref.sync import async_to_sync
from django.core.serializers import serialize
from celery import shared_task


@shared_task
@receiver(post_save, sender=PostModel)
def send_post_to_telegram_channel(sender, instance, created, **kwargs):
    if created:
        post_data = {
            'title': instance.title,
            'url_address': instance.get_absolute_url(),
        }
        send_post_task.delay(post_data)
    print('Send message to telegram channel')
    return 'Send message to telegram channel'
