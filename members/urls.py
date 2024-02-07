from django.urls import path
from .views import login_view, logout_request, register_view, create_profile_view, edit_profile_view, delete_profile, profile_view, star_view, like_view



urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_request, name='logout'),
    path('create_profile/<int:id_user>/', create_profile_view, name='create-profile'),
    path('edit_profile/<int:id_user>/', edit_profile_view, name='edit-profile'),
    path('delete_profile/<int:id_user>/', delete_profile, name='delete-profile'),
    path('profile/<int:id_user>/', profile_view, name='profile'),
    path('star/<int:id_user>/<int:ball>/', star_view, name='star-account'),
    path('likes/<int:id_user>/', like_view, name='likes'),
]

