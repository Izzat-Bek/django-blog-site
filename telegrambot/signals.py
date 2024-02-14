from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TelegramBot


@receiver(post_save, sender=TelegramBot)
def check_telegram_bot(sender, instance, created, **kwargs):
    if created or not instance.error_message:
        if instance.check_telegram_token() and instance.get_chat_id():
            instance.save()
            
    
        