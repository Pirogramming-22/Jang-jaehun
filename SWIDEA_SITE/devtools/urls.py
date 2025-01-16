from django.urls import path
from devtools import views

# html에서 {% url 'devtools:main' %} 이런식으로 사용할 수 있음
app_name = 'devtools'

urlpatterns = [
    path('', views.main, name='main'),
    path('devtool_create', views.devtool_create, name='devtool_create'),
    path('devtool_detail/<int:pk>', views.devtool_detail, name='devtool_detail'),
    path('devtool_delete/<int:pk>', views.devtool_delete, name='devtool_delete'),
    path('devtool_update/<int:pk>', views.devtool_update, name='devtool_update'),
]