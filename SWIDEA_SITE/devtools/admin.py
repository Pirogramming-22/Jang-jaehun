from django.contrib import admin
from .models import Devtool

# 모델 등록
@admin.register(Devtool)
class DevtoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kind', 'content')