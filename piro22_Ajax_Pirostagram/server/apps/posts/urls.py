from django.urls import path
from apps.posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('like_ajax/', views.like_ajax, name='like_ajax'), # 좋아요 토글
    path('<int:post_id>/comments/', views.post_comments, name='post_comments'), # 댓글 가져오기 및 추가
    path('<int:post_id>/comments/<int:comment_id>/', views.delete_comment, name='delete_comment'), # 댓글 삭제
]
