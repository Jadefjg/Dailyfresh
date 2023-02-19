from haystack.views import SearchView
from apps.goods.models import GoodsInfo


class MySeachView(SearchView):

    def extra_context(self):
        """
            重载 extra_context 来添加额外的 context 内容
        """

        # 查询新品
        newgood = GoodsInfo.objects.all().order_by('-id')[:2]
        # 保持原来 context 不变
        context = super(MySeachView,self).extra_context()
        # 新增 context
        context['page_name'] = 1
        context['title'] = '查询结果'
        context['newgood'] = newgood
        return context