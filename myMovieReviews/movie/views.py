from django.shortcuts import render
from .forms import MovieForm

# 영화 목록 페이지
def movie_list(request):
    return render(request, 'movie/movie_list.html')

# 영화 상세 페이지
def movie_detail(request, pk):
    return render(request, 'movie/movie_detail.html', {'movie_id': pk})

# 영화 생성/수정 폼 페이지
def movie_form(request):
    form = MovieForm()
    return render(request, "movie/movie_form.html", {"form": form, "form_title": "Movie review 🎬"})

# 영화 삭제 페이지
def movie_delete(request, pk):
    return render(request, 'movie/movie_delete.html', {'movie_id': pk})