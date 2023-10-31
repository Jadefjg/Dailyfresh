from django.urls import path,re_path
from apps.goods.views import IndexView,DetailView,ListView
# from apps.goods.search_views import MySeachView

app_name = 'apps.goods'

urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    re_path('^goods/(?P<goods_id>\d+)$', DetailView.as_view(), name='detail'),
    re_path('^goods/list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'),
    # re_path('^goods/(?P<goods_id>\d+)$', MySeachView.as_view(), name='seachview'),
]


