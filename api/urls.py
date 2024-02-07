from django.urls import path
from .views import PostModelAPIView


urlpatterns = [
    path('posts/', PostModelAPIView.as_view()),
]

