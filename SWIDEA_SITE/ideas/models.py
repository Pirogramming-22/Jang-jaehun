from django.db import models
from devtools.models import Devtool

class Idea(models.Model):
    title = models.CharField('제목', max_length=24)
    image = models.ImageField('이미지', upload_to='ideas/%Y%m%d', blank=True)
    content = models.TextField('내용', max_length=100)
    interest = models.IntegerField('관심도', default=0)
    # devtool = models.CharField('개발툴', max_length=24) # Devtool 모델을 참조하지 않고 문자열로 저장
    devtool = models.ForeignKey(Devtool, verbose_name='개발툴', on_delete=models.CASCADE) # Devtool 모델을 참조