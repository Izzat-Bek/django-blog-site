from blog.models import PostModel
from django.contrib.auth.models import User
from members.models import Profile
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('id', 'title', 'author_id', 'likes', 'view_profile')


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'likes', 'confidentiality')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class PostArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
