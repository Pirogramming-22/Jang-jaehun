from django.urls import path
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
]
