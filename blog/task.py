from celery import shared_task
from telegram import Bot
from telegram.constants import ParseMode
import logging
from django.conf import settings
from .models import PostModel


@shared_task
async def send_message_to_telegram_channel(news):
    
    bot = Bot(token=settings.BOT_API)
    channel_id = '@izzat_ansajfsnafis'
    url = f'http://127.0.0.1:8016/article/{news.id}'
    url_ad = url.replace('_', r'\_').replace('*', r'\*').replace('[', r'\[').replace(']', r'\]')
    message = f'{news.title} \nPodrobno: [URL]({url_ad})'
    
    try:
        await bot.send_message(channel_id, message, parse_mode=ParseMode.MARKDOWN)
        print(f'News {news.title} sent to {channel_id}')
    except Exception as e:
        logging.error(e)

