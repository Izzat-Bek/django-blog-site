from django.shortcuts import render
from rest_framework import generics
from blog.models import PostModel
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.parsers import MultiPartParser



# class PostModelAPIView(generics.ListCreateAPIView):
#     queryset = PostModel.objects.all().order_by('-date_ad')[1:3]
#     serializer_class = PostSerializer
    
    
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
    
