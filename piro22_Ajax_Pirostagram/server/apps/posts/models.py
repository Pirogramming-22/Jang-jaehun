from django.db import models
from django.contrib.auth.models import User  # Django 기본 User 모델 가져오기

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # 게시물과의 관계
    # user = models.CharField(max_length=50)  # 댓글 작성자 (User 모델 연결 없이 간단히 CharField로 구현)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='comments')  # 기본값으로 admin 유저 사용
    text = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 댓글 작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 댓글 수정 시간

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"