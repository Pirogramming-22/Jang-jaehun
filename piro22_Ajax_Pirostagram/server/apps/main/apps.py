from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.main' # 앱 경로가 'apps.main'으로 지정되어야 함
