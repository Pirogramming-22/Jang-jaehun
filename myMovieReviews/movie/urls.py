from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    # 영화 목록
    path('', views.movie_list, name='movie_list'),

    # 영화 상세
    path('<int:id>', views.movie_detail, name='movie_detail'),

    # 영화 생성
    path('create', views.movie_form, name='movie_create'),

    # 영화 수정
    path('update/<int:id>', views.movie_form, name='movie_update'),

    # 영화 삭제
    path('delete/<int:id>', views.movie_detail, name='movie_delete'),
]