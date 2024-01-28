from django.contrib import admin
from .models import Profile, StarModel



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'url_website', 'url_instagram', 'url_telegram', 'url_github')
    list_display_links = ('user',)
    search_fields = ('user',)
    

@admin.register(StarModel)
class StarModelAdmin(admin.ModelAdmin):
    list_display = ('user_acc', 'user', 'star_num', 'id')
    list_display_links = ('user',)
    search_fields = ('user_acc', 'user')
    ordering = ('-id',)
    
