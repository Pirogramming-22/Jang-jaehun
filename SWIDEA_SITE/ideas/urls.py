from django.urls import path
from ideas import views

# html에서 {% url 'ideas:main' %} 이런식으로 사용할 수 있음
app_name = 'ideas'

urlpatterns = [
    path('', views.main, name='main'),
    path('idea_create', views.idea_create, name='idea_create'),
    path('idea_detail/<int:pk>', views.idea_detail, name='idea_detail'),
    path('idea_delete/<int:pk>', views.idea_delete, name='idea_delete'),
    path('idea_update/<int:pk>', views.idea_update, name='idea_update'),
]