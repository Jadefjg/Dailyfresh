from django.contrib import admin
from django.core.cache import cache
from apps.goods.models import TypeInfo, GoodsType, IndexPromotionBanner, IndexGoodsBanner, IndexTypeGoodsBanner, GoodsSKU, GoodsSPU, GoodsImage, GoodsInfo

# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """薪资或更新列表的数据时调用"""
        super().save_model(request, obj, form, change)

        # 发出任务，让 celery worker 重新生成首页静态页面
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()

        # 清楚缓存
        cache.delete('index_page_data')

    def delete_model(self, request, obj):
        """新增或更新列表中的数据时调用"""
        super().delete_model(request, obj)

        # 发出任务，让 celery workers 重新生成首页静态页面
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()
        # 清楚缓存
        cache.delete('index_page_data')


class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


class GoodsTypeAmin(BaseModelAdmin):
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass


class TypeInfoAdmin(BaseModelAdmin):
    pass


class GoodsInfoAmin(BaseModelAdmin):
    pass


admin.site.register(GoodsType, GoodsTypeAmin)
admin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
admin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(IndexTypeGoodsBanner, IndexGoodsBannerAdmin)
admin.site.register(GoodsImage)
admin.site.register(GoodsSPU)
admin.site.register(GoodsSKU)
admin.site.register(GoodsInfo)
admin.site.register(TypeInfo)

