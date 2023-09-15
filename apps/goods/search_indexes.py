from haystack import indexes                         # 定义索引类
from apps.goods.models import GoodsInfo, GoodsSKU    # 导入模型类

# 指定对于某个类的某些数据建立索引。 索引类名格式：模型类名+index


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段，指定根据表中哪些字段建立索引文件
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return GoodsSKU

    # 建立索引的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()


