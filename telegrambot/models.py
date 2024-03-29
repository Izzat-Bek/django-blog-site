from django.db import models
from myblog.settings import config
from members.models import Profile
import requests


default_chat_id = config('TELEGRAM_CHANNEL')
default_token_id = config('BOT_TOKEN')


class TelegramBot(models.Model):
    token = models.CharField(max_length=255, default=default_token_id)
    chat_id = models.CharField(max_length=100, default=default_chat_id)
    username = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Author_post')
    error_message = models.CharField(max_length=555, blank=True, null=True)
    

    def __str__(self):
        return f'self.username'
    
    
    def check_telegram_token(self):
        try:
            url = f'https://api.telegram.org/bot{self.token}/getMe'
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 or data['ok'] == True:
                self.error_message = 'Token is successfully added'
                return True
            else:
                self.error_message = 'Token is not added please check token'
                return False
        except Exception as e:
            self.error_message = 'Token is not added please don\'t use bot token'
            return False
        
    
    def get_chat_id(self):
        try:
            url = f'https://api.telegram.org/bot{self.token}/getChat?chat_id={self.chat_id}'
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 or data['ok'] == True:
                self.error_message = 'Chat id is successfully added'
                return True
            else:
                self.error_message = 'Chat id is not added please check chat id'
                return False
        except Exception as e:
            self.error_message = 'Chat id is not added please don\'t use bot token'
            return False
        
        