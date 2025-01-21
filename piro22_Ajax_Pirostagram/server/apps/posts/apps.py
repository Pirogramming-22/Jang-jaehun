from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.posts' # 앱 경로가 'apps.posts'으로 지정되어야 함
