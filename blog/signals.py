from .models import PostModel
from django.dispatch import receiver
from django.db.models.signals import post_save
from .task import send_message_to_telegram_channel as send_post_task


@receiver(post_save, sender=PostModel)
async def send_post_to_telegram_channel(sender, instance, created, **kwargs):
    if created:
        return await send_post_task(instance)
    print('Send message to telegram channel')
    return 'Send message to telegram channel'
