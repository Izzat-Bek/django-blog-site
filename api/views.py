from django.shortcuts import render
from rest_framework import generics
from blog.models import PostModel, Category, StarModel as Star
from .serializers import (PostSerializer, PostArticleSerializer, ProfilesSerializer, 
                          ProfileArticleSerializer, CategorySerializer, StarPostSerializer,
                          TelegrammBotSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.parsers import MultiPartParser
from members.models import Profile, StarModel
from telegrambot.models import TelegramBot


    
class PostModelAPIView(APIView):
    
    # parser_classes = (MultiPartParser,)
    
    def get(self, request):
        posts = PostModel.objects.all().order_by('-id')
        post =PostSerializer(posts, many=True)
        return Response(post.data)
    
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


class PostArticleAPIView(APIView):
    def get(self, request, post_id):
        try:
            post = PostModel.objects.get(id=post_id)
            serializer = PostArticleSerializer(post)
            return Response(serializer.data)
        except PostModel.DoesNotExist:
            return Response({'error': 'Post not found'}, status=404)
        

class ProfilesAPIView(APIView):
    def get(self, request):
        profiles = Profile.objects.all().order_by('-id')
        serializer = ProfilesSerializer(profiles, many=True)
        return Response(serializer.data)
    
    

class ProfilesArticleAPIView(APIView):
    def get(self, request, profile_id):
        try:
            profile = Profile.objects.get(id=profile_id)
            serializer = ProfileArticleSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=404)
        

class CategoryAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)
    
    

class CategoryArticleAPIView(APIView):
    
    def get(self, requests, id_cat):
        category = Category.objects.get(id=id_cat)
        posts = PostModel.objects.filter(category=category)
        serializers = PostSerializer(posts, many=True)
        return Response(serializers.data)
    

class StarPostAPIView(APIView):
    
    def get(self, request):
        star = Star.objects.all()
        serializers = StarPostSerializer(star, many=True)
        return Response(serializers.data)


class TelegrammBotAPIView(APIView):
    
    def get(self, request):
        bot = TelegramBot.objects.all()
        serializers = TelegrammBotSerializer(bot, many=True)
        return Response(serializers.data)
    