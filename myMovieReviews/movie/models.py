from django.db import models

# Create your models here.
class Movie(models.Model):
    # 영화 제목
    title = models.CharField(max_length=100)

    # 개봉년도
    release_year = models.IntegerField()

    # 장르 목록
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('MeloDrama', 'MeloDrama'),
        ('SF', 'SF'),
        ('Horror', 'Horror'),
    ]

    # 장르
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)

    # 별점
    rating = models.FloatField()

    # 러닝타임
    runtime = models.IntegerField()

    # 리뷰
    review = models.TextField()

    # 감독
    director = models.CharField(max_length=100)

    # 배우
    actors = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title