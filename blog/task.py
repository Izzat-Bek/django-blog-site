from telegram import Bot
from myblog.settings import config
from .views import url_address
import logging
from telegram.constants import ParseMode
from celery import shared_task



@shared_task
async def send_message_to_telegram_channel(post):
    post_title = post['title']
    post_url = post['url_address']
    bot = Bot(token=config('BOT_TOKEN'))
    channel_id = config('TELEGRAM_CHANNEL')
    url = f'http://127.0.0.1:8000{post_url}' 
    url_ad = url.replace('_', r'\_').replace('*', r'\*').replace('[', r'\[').replace(']', r'\]')
    message = f'{post_title} \nPodrobno: [URL]({url_ad})'
    try:
        await bot.send_message(channel_id, message, parse_mode=ParseMode.MARKDOWN)
        print(f'Post {post_title} sent to telegram chanell as {channel_id}')
    except Exception as e:
        print(f'{e}')
        logging.error(e)
        