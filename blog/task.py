from telegram import Bot
from myblog.settings import config
import logging
from telegram.constants import ParseMode
from celery import shared_task



@shared_task
async def send_message_to_telegram_channel(post):
    post_title = post['title']
    post_url = post['url_address']
    bot_token = post['token']
    channel_id = post['chat_id']
    if channel_id is not None and bot_token is not None:
        bot = Bot(token=bot_token)
        url = f'http://127.0.0.1:8000{post_url}' 
        url_ad = url.replace('_', r'\_').replace('*', r'\*').replace('[', r'\[').replace(']', r'\]')
        message = f'{post_title} \nPodrobno: [URL]({url_ad})'
        try:
            await bot.send_message(channel_id, message, parse_mode=ParseMode.MARKDOWN)
            print(f'\n\nPost {post_title} sent to telegram chanell as {channel_id}\n\n')
        except Exception as e:
            print(f'{e}')
            logging.error(e)
            

@shared_task
async def send_delete_post(post):
    post_title = post['title']
    bot_token = post['token']
    channel_id = post['chat_id']
    if channel_id is not None and bot_token is not None:
        bot = Bot(token=bot_token)
        message = f'{post_title} \nIs deleted'
        try:
            await bot.send_message(channel_id, message, parse_mode=ParseMode.MARKDOWN)
            print(f'\n\nPost {post_title} sent to telegram chanell as {channel_id}\n\n')
        except Exception as e:
            print(f'{e}')
            logging.error(e)
            