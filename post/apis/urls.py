from django.urls import path
from .views import create, get

urlpatterns = [
    path('get/', get.get_posts_view.as_view(),name='get_posts'),
    path('create/', create.create_post_view.as_view(),name='create_posts'),
]