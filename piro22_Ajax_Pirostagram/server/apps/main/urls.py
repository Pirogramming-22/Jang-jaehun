from django.urls import path
from apps.main import views

# html에서 {% url 'posts:main' %} 이런식으로 사용할 수 있음
app_name = 'main'

urlpatterns = [    
    path('', views.main, name='main'),
]