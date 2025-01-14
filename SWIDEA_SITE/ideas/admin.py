from django.contrib import admin
from .models import Idea

# 모델 등록
@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'interest', 'devtool')  # 관리자 목록에 표시할 필드
    search_fields = ('title', 'content')  # 검색 필드