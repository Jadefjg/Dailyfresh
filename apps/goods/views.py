from django.shortcuts import render, redirect, reverse
from django_redis import get_redis_connection
from django.core.paginator import Paginator
from django.views.generic.base import View
from django.core.cache import cache

from apps.goods.models import GoodsType, IndexGoodsBanner, IndexTypeGoodsBanner, IndexPromotionBanner, GoodsSKU
from apps.order.models import OrderGoods


# Create your views here.

# goods/index
class IndexView(View):
    """首页"""

    def get(self,request):
        """首页"""
        # 获取用户信息
        user = request.user

        # 判断缓存
        try:
            context = cache.get('index_page_data')
        except Exception as e:
            context = None

        if context is None:
            # 没有缓存数据
            # 获取商品种类信息
            types = GoodsType.objects.all()

            # 获取首页轮播商品信息
            goods_banners = IndexGoodsBanner.objects.all().order_by('index')

            # 获取首页促销商品信息
            promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

            # 获取分类商品展示信息
            for type in types:
                image_goods_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1)
                font_goods_banners = IndexGoodsBanner.objects.filter(type=1, display_type=0)
                type.image_goods_banners = image_goods_banners
                type.font_goods_banners = font_goods_banners

            # 组织上下文
            context = {
                'types': types,
                'goods_banners': goods_banners,
                'promotion_banners': promotion_banners,
                # 'type_goods_banners': type_goods_banners,
                # 'cart_count': cart_count
            }
            # 设置缓存
            cache.set('index_page_data', context, 3600)

        # 获取购物车中商品数量
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_{0}'.format(user.id)
            cart_count = conn.hlen(cart_key)
        context.update(user=user,cart_count=cart_count)
        return render(request,'df_goods/index.html',context)


# goods/detail/sku_id
class DetailView(View):
    """详情页面"""
    def get(self,request,goods_id):
        """显示详情页面"""
        # 获取商品 SKU 信息
        try:
            sku = GoodsSKU.objects.get(id=goods_id)
        except GoodsSKU.DoesNotExist:
            return redirect(reverse('goods:detail'))

        # 获取商品分类消息
        types = GoodsType.objects.all()

        # 获取商品的评论信息
        sku_orders = OrderGoods.objects.filter(sku=sku)

        # 获取新商信息
        new_skus = GoodsSKU.objects.filter(type=sku.type).order_by('-create_time')[:2]

        # 获取同一个 SPU 的商品
        same_spu_skus = GoodsSKU.objects.filter(goods_spu=sku.goods_spu).exclude(id=goods_id)

        # 获取用户购物车中的商品数目
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_{}'.format(user.id)
            cart_count = conn.hlen(cart_key)

            # 添加用户的历史浏览记录
            conn = get_redis_connection('default')
            history_key = 'history_{}'.format(user.id)
            conn.lrem(history_key,0,goods_id)
            conn.lpush(history_key,goods_id)

            # 只保存用户的最新浏览的 5 条数据
            conn.ltrim(history_key,0,4)

        # 组织上下文
        context = {
            'sku':sku,
            'types':types,
            'sku_orders':sku_orders,
            'new_skus':new_skus,
            'same_spu_skus':same_spu_skus,
            'cart_count':cart_count
        }

        # 使用模板
        return render(request,'df_goods/detail.html',context)


# goods/list/type_id/页码?sort=排序方式
class ListView(View):
    """列表页"""
    def get(self,request,type_id,page):
        """显示列表页"""
        # 获取种类信息
        try:
            type = GoodsType.objects.get(id=type_id)
        except GoodsType.DoesNotExist:
            return redirect(reverse('good:index'))

        """
            获取排序方式
            sort = default  按照默认的 id 排序
            sort = price    按照商品价格
            sort = hot      按照商品销量排序
        """
        sort = request.GET.get('sort')
        if sort == 'price':
            skus = GoodsSKU.objects.filter(types=type).order_by('price')
        elif sort == 'hot':
            skus = GoodsSKU.objects.filter(type=type).order_by('-sales')
        else:
            sort = 'default'
            skus = GoodsSKU.objects.filter(type=type).order_by('-id')

        # 对商品进行分页
        paginator = Paginator(skus,1)

        # 获取第 page 页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        # 获取第 page 页的paginator.page实例对象
        skus_page = paginator.page(page)

        # todo：进行页码控制 ，页面上最多显示 5 个页面
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1,num_pages + 1)
        elif page <= 3:
            pages = range(1,6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4,num_pages + 1)
        else:
            pages = range(page - 2,page + 3)

        # 获取商品的分类信息
        types = GoodsType.objects.all()

        # 获取新商信息
        new_skus = GoodsSKU.objects.filter(type=type).order_by('-create_time')[:2]

        # 实现用户购物车中的商品数目
        user = request.user
        cart_count = 0
        if user.is_authenticated:
            # 用户已登录
            conn = get_redis_connection('default')
            cart_key = 'cart_{}'.format(user.id)
            cart_count = conn.hlen(cart_key)

        # 组织上下文
        context = {
            'type': type,
            'skus_page': skus_page,
            'types': types,
            'new_skus':new_skus,
            'cart_count':cart_count,
            'sort':sort,
            'pages':pages,
        }

        return render(request,'df_goods/list.html',context)


# def index(request):
#     """
#         index 函数负责查询页面中需要展示的商品内容，主要是每类最新的 4 种商品和 4种点击率最高的商品，每类商品需要查询2次
#     """
#     fruit = GoodsInfo.objects.filter(gtype__id=1).order_by("-id")[:4]
#     fruit2 = GoodsInfo.objects.filter(gtype__id=1).order_by("-gclick")[:3]
#     fish = GoodsInfo.objects.filter(gtype_id=2).order_by("-id")[:4]
#     fish2 = GoodsInfo.objects.filter(gtype_id=2).order_by("-gclick")[:3]
#     meat = GoodsInfo.objects.filter(gtype_id=2).order_by("-id")[:4]
#     meat2 = GoodsInfo.objects.filter(gtype_id=2).order_by("-gclick")[:4]
#     egg = GoodsInfo.objects.filter(gtype_id=2).order_by("-id")[:4]
#     egg2 = GoodsInfo.objects.filter(gtype_id=2).order_by("-gclick")[:4]
#     vegetables = GoodsInfo.objects.filter(gtype_id=2).order_by("-id")[:4]
#     vegetables2 = GoodsInfo.objects.filter(gtype_id=2).order_by("-gclick")[:4]
#     frozen = GoodsInfo.objects.filter(gtype_id=2).order_by("-id")[:4]
#     frozen2 = GoodsInfo.objects.filter(gtype_id=2).order_by("-gclick")[:4]
#     context = {'title':'首页','fruit':fruit,
#                'fish':fish,'meat':meat,'egg':egg,
#                'vegetables':vegetables,'frozen':frozen,
#                'fruit2':fruit2,'fish2':fish2,'meat2':meat2,
#                'egg2':egg2,'vegetables2':vegetables2,'frozen2':frozen2,
#                'guest_cart':1,'page_name':0,}
#     # 返回渲染模板
#     return render(request,'goods/index.html',context)
#
# # 商品列表
# def goodList(request,typeid,pageid,sort):
#     """
#         goodlist 函数负责展示某类商品的信息
#         url 中的参数依次代表
#         typeid:商品类型id；selectid：查询条件id，1为根据id查询，2为根据价格查询，3为根据点击查询
#     """
#
#     # 获取最新发布的商品
#     newgood = GoodsInfo.objects.all().order_by('id')[:2]
#     # 根据条件查询所有商品
#     if sort == '1':     # 按最新
#         sumGoodList = GoodsInfo.objects.filter(gtype_id=typeid).order_by('-id')
#     elif sort == '2':   # 按价格
#         sumGoodList = GoodsInfo.objects.filter(gtype_id=typeid).order_by('gprice')
#     elif sort == '3':   # 按点击量
#         sumGoodList = GoodsInfo.objects.filter(gtype_id=typeid).filter('-gclick')
#
#     # 分页
#     paginator = Paginator(sumGoodList,15)
#     goodList = paginator.page(int(pageid))
#     pindexlist = paginator.page_range
#     # 确定商品的类型
#     goodtype = TypeInfo.objects.get(id=typeid)
#     context = {'title':'商品详情','list':1,
#                'guest_cart':1,'goodtype':goodtype,
#                'newgood':newgood,'goodList':goodList,
#                'typeid':typeid,'sort':sort,
#                'pindexlist':pindexlist,'pageid':int(pageid),
#     }
#     # 渲染返回结果
#     return render(request,'goods/list.html',context)
#
# def detail(request,id):
#     goods = GoodsInfo.objects.get(pk=int(id))
#     goods.gclick = goods.gclick+1
#     goods.save()
#     # 查询当前商品的类型
#     goodtype = TypeInfo.objects.get(goodsinfo__id=id)
#     news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
#     context = {'title':goods.gtype.ttitle,'guest_cart':1,
#                'g':goods,'newgood':news,'id':id,
#                'isDetail':True,'list':1,'goodtype':goodtype}
#     response = render(request,'good/detail.html',context)
#
#     # 使用 cookies 记录最近浏览的商品id
#
#     # 获取 cookies
#     goods_ids = request.COOKIES.get('goods_ids','')
#     # 获取当前点击商品 id
#     goods_id = '%d'%goods.id
#     if goods_ids !='':
#         # 分割每个商品的 id
#         goods_id_list=goods_ids.split(',')
#         # 判断商品是否已经存在于列表
#         if goods_id_list.count(goods_id)>=1:
#             # 存在则移除
#             goods_id_list.remove(goods_id)
#         # 在第一位添加
#         goods_id_list.insert(0,goods_id)
#         # 判断列表数是否超过5个
#         if len(goods_id_list)>=6:
#             # 超过五个则删除第6个
#             del goods_id_list[5]
#         # 添加商品 id 到cookies
#         goods_ids = ','.join(goods_id_list)
#     else:
#         # 第一次添加，直接追加
#         goods_ids = goods_id
#     response.set_cookie('goods_ids',goods_ids)
#
#     return response
