from django.db import models

class Devtool(models.Model):
    name = models.CharField('이름', max_length=24)
    kind = models.CharField('종류', max_length=24)
    content = models.TextField('내용', max_length=100)
