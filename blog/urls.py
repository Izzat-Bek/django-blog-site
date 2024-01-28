from django.urls import path
from .views import (home_view, category_view, article_detail, add_star, 
                    comment_view, comment_username_view,
                    delete_post_view, contact_view,
                    add_post_view, like_view_jquere, like_home_view_jquere)

urlpatterns = [
    path('', home_view, name='home'),
    path('category/<int:id_cat>/', category_view, name='category'),
    path('article/<int:id_post>/', article_detail, name='article'),
    path('add_star/<int:id_post>/<int:ball>/', add_star, name='add_star'),
    path('comment/<int:id_post>/<int:id_user>/', comment_view, name='comment-username'),
    path('comment/<int:id_post>/', comment_username_view, name='comment'),
    path('like/<int:post_id>/', like_view_jquere, name='like'),
    path('delete/<int:id_post>/', delete_post_view, name='delete'),
    path('like-home/<int:post_id>/', like_home_view_jquere, name='like-home'),
    path('contact/', contact_view, name='contact'),
    path('add-post/', add_post_view, name='add-post'),
]

