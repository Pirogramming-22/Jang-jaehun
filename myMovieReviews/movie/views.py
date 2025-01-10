from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

# 영화 목록 페이지
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movie': movies})

# 영화 상세 페이지
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie/movie_detail.html', {'movie_id': pk}, {'movie': movie})

# 영화 생성/수정 폼 페이지
def movie_form(request, pk=None):
    if pk:
        movie = get_object_or_404(Movie, pk=pk)
        if request.method == "POST":
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save() # 수정된 데이터 저장
                return redirect('movie:movie_list')
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
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect('movie:movie_list')
    return render(request, 'movie/movie_detail.html', {'movie_id': pk}) # 수정 필요