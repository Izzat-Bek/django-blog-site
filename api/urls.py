from django.urls import path
from .views import PostModelAPIView, PostArticleAPIView, ProfilesAPIView, ProfilesArticleAPIView


urlpatterns = [
    path('posts/', PostModelAPIView.as_view()),
    path('post/<int:post_id>/article/', PostArticleAPIView.as_view()),
    path('profiles/', ProfilesAPIView.as_view()),
    path('profile/<int:profile_id>/article/', ProfilesArticleAPIView.as_view()),
]

