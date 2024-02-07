from rest_framework import serializers
from blog.models import PostModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ('title', 'author_id', 'likes', 'view_profile')
