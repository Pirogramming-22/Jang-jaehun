from django.db import models
from devtools.models import Devtool
from django.contrib.auth.models import User  # User 모델 참조

class Idea(models.Model):
    title = models.CharField('제목', max_length=24)
    image = models.ImageField('이미지', upload_to='ideas/%Y%m%d', blank=True)
    content = models.TextField('내용', max_length=100)
    interest = models.IntegerField('관심도', default=0)
    devtool = models.ForeignKey(Devtool, verbose_name='개발툴', on_delete = models.CASCADE) # Devtool 모델을 참조

# IdeaStar 모델 추가
class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)  # 찜한 아이디어
    session_key = models.CharField(max_length=255)  # 세션 키를 저장
    created_at = models.DateTimeField(auto_now_add=True)  # 찜한 날짜

    class Meta:
        unique_together = ('idea', 'session_key')  # 동일 세션에서 중복 찜 방지