from django.urls import path
from apps.cart.views import CartAddView,CartInfoView,CartUpdateView,CartDeleteView

# app_name = 'cart'
app_name = 'apps.cart'

urlpatterns = [
    path('add', CartAddView.as_view(), name='add'),           # 购物车记录添加
    path('', CartInfoView.as_view(), name='show'),        # 购物车页面显示
    path('update', CartUpdateView.as_view(), name='update'),  # 购物车记录更新
    path('delete', CartDeleteView.as_view(), name='delete'),  # 购物车记录删除
]


"""


后端：
    model - view - url


前端：
    css - html - js


"""


