from django.db import models

class Devtool(models.Model):
    name = models.CharField('이름', max_length=24)
    kind = models.CharField('종류', max_length=24)
    content = models.TextField('내용', max_length=400, blank=True)

    def __str__(self):
        return self.name  # 이름 필드를 표시하도록 설정
