from django.apps import AppConfig


class GoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.goods'
    verbose_name = '商品'
