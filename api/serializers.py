from blog.models import PostModel, Category, StarModel
from django.contrib.auth.models import User
from members.models import Profile, StarModel as Star
from rest_framework import serializers
from telegrambot.models import TelegramBot


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('id', 'title', 'author_id', 'likes', 'view_profile')


class PostsStarSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = PostModel
        fields = ('id', 'title')
        

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'likes', 'confidentiality')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ProfileArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('bio', 'user')


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name')


class PostArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = PostModel
        fields = '__all__'

class StarPostSerializer(serializers.ModelSerializer):
    post = PostsStarSerializers()
    profile = ProfileArticleSerializer()
    class Meta:
        model = StarModel
        fields = ('id', 'post', 'profile', 'star_num')


class TelegrammBotSerializer(serializers.ModelSerializer):
    username = ProfilesSerializer()
    class Meta:
        model = TelegramBot
        fields = '__all__'
    