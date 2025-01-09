from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(label="제목", max_length=100)
    release_year = forms.IntegerField(label="개봉년도")
    genre = forms.ChoiceField(
        label="장르",
        choices=[
            ("", "--------"), 
            ("Action", "Action"), 
            ("Comedy", "Comedy"), 
            ("Drama", "Drama"),
            ("SF", "SF")
        ]
    )
    rating = forms.FloatField(label="별점")
    runtime = forms.IntegerField(label="러닝타임")
    review = forms.CharField(label="리뷰", widget=forms.Textarea)
    director = forms.CharField(label="감독", max_length=100)
    actors = forms.CharField(label="배우", max_length=200)