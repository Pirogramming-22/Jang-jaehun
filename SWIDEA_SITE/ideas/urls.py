from django.urls import path
from ideas import views

# html에서 {% url 'ideas:main' %} 이런식으로 사용할 수 있음
app_name = 'ideas'

urlpatterns = [
    path('', views.main, name='main'),
    path('idea-create', views.idea_create, name='idea_create'),
    path('idea-detail/<int:pk>', views.idea_detail, name='idea_detail'),
    path('idea-delete/<int:pk>', views.idea_delete, name='idea_delete'),
    path('idea-update/<int:pk>', views.idea_update, name='idea_update'),
    path('toggle_star/<int:pk>/', views.toggle_star, name='toggle_star'), # 찜하기 기능
    path('interest-plus/<int:pk>/', views.interest_plus, name='interest_plus'), # 관심도 증가
    path('interest-minus/<int:pk>/', views.interest_minus, name='interest_minus'), # 관심도 감소
]