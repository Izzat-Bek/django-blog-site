from django.contrib import admin
from .models import TelegramBot


@admin.register(TelegramBot)
class TelegramBotAdmin(admin.ModelAdmin):
   list_display = ('username', 'token', 'chat_id')
   list_display_links = ('token',)
   search_fields = ('token', 'chat_id')
   