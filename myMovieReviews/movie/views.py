from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

# 영화 목록 페이지
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

# 영화 상세 페이지
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    runtime_hours = movie.runtime // 60
    runtime_minutes = movie.runtime % 60
    return render(request, 'movie/movie_detail.html', {'movie': movie,'runtime_hours': runtime_hours,'runtime_minutes': runtime_minutes})

# 영화 생성/수정 폼 페이지
def movie_form(request, id=None):
    if id:
        movie = get_object_or_404(Movie, id=id)
        if request.method == "POST":
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save() # 수정된 데이터 저장
                return redirect('movie:movie_detail', id)
        else: # 폼이 유효하지 않은 경우
            form = MovieForm(instance=movie)
    else:
        if request.method == "POST":
            form = MovieForm(request.POST)
            if form.is_valid():
                form.save() # 새 데이터 저장
                return redirect('movie:movie_list')
        else: # 폼이 유효하지 않은 경우
            form = MovieForm()

    return render(request, "movie/movie_form.html", {"form": form, "form_title": "Movie review 🍿"})

# 영화 삭제 페이지
def movie_delete(request, id):
    if request.method == "POST": # POST 요청인 경우만 처리
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return redirect('movie:movie_list')
    else: # GET 요청이 들어오면 목록 페이지로 리다이렉트
        return redirect('movie:movie_list')