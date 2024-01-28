from django.contrib import admin
from .models import PostModel, Category, CommentModel, StarModel

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_ad')
    list_display_links = ('title',)
    search_fields = ('title', 'category')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('post', 'username', 'date_ad')
    list_display_links = ('post', 'username')
    search_fields = ('post', 'username')
    

@admin.register(StarModel)
class StarModelAdmin(admin.ModelAdmin):
    list_display = ('post', 'profile', 'star_num')
    list_display_links = ('post', 'profile')
    search_fields = ('post', 'profile')
