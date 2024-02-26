from django.urls import path
from .views import (PostModelAPIView, PostArticleAPIView, ProfilesAPIView, 
                    ProfilesArticleAPIView, CategoryAPIView, CategoryArticleAPIView,
                    StarPostAPIView, TelegrammBotAPIView)

urlpatterns = [
    path('posts/', PostModelAPIView.as_view()),
    path('post/<int:post_id>/article/', PostArticleAPIView.as_view()),
    path('profiles/', ProfilesAPIView.as_view()),
    path('profile/<int:profile_id>/article/', ProfilesArticleAPIView.as_view()),
    path('categories/', CategoryAPIView.as_view()),
    path('category/<int:id_cat>/article/', CategoryArticleAPIView.as_view()),
    path('star/posts/', StarPostAPIView.as_view()),
    path('telegram/bots/', TelegrammBotAPIView.as_view()),
]

