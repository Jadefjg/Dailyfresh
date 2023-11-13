import os
import json
import requests

from datetime import datetime

from django.urls import reverse
from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django_redis import get_redis_connection
from django.shortcuts import render, redirect
from django.views.generic.base import View, logger

from apps.user.models import Address
from apps.goods.models import GoodsSKU
from utils.mixin import LoginRequiredMixin
from apps.order.models import OrderInfo, OrderGoods

from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.request.AlipayTradeQueryRequest import AlipayTradeQueryRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest


# /order/place
class OrderPlaceView(LoginRequiredMixin,View):
    """提交订单页面显示"""
    def post(self,request):
        """提交订单页面显示"""

        # 获取登录的用户
        user = request.user

        # 获取参数 sku_ids
        sku_ids = request.POST.getList('sku_ids')
        # 校验数据
        if not sku_ids:
            # 跳转到购物车页面
            return redirect(reverse('cart:show'))

        # 遍历 sku_ids 获取用户购买的商品信息
        conn = get_redis_connection('default')
        cart_key = 'cart_{}'.format(user.id)

        total_count = 0
        total_price = 0
        skus = list()
        for sku_id in sku_ids:
            sku = GoodsSKU.objects.get(id=sku_id)
            count = conn.hget(cart_key,sku_id)
            # 计算商品小计
            amount = int(count) * sku.price
            # 动态给 sku 增加 amount, count属性
            sku.count = count        # 动态给 sku 增加属性 amount， 保存购买商品数量
            sku.amount = amount     # 动态给 sku 增加属性 amount， 保存购买商品的小计

            skus.append(sku)
            total_count += int(count)   # 商品总数
            total_price += amount       # 商品总价

        # 运费：实际开发需要单独设计，属于一个子系统
        transit_price = 10      # 写死

        # 实付款
        total_pay = total_price + transit_price

        # 获取用户的文件地址
        addrs = Address.objects.filter(user=user)

        # 组织上下文
        sku_ids = ','.join(sku_ids)
        context = {
            'skus': skus,
            'total_count': total_count,
            'total_price': total_price,
            'transit_price': transit_price,
            'total_pay': total_pay,
            'addrs': addrs,
            'sku_ids': sku_ids,
        }

        # 使用模板
        return render(request,'df_order/place_order.html',context)


# ajax post
# 地址id：addr_id,支付方式： pay_method,商品id字符串： sku_ids
# /order/commit
# 悲观锁
class OrderCommitView(View):
    """订单创建"""
    @transaction.atomic
    def post(self,request):
        """订单创建"""
        # 判断用户登录
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登陆'})

        # 接受参数
        addr_id = request.POST.get('add_id')
        pay_method = request.POST.get('pay_method')
        sku_ids = request.POST.get('sku_ids')

        # 校验参数
        if not all([addr_id,pay_method,sku_ids]):
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        # 校验支付方式
        if pay_method not in OrderInfo.PAY_METHOD.keys():
            print(pay_method,type(pay_method))
            return JsonResponse({'res': 2, 'errmsg': '无效支付方式'})

        # 校验地址
        try:
            addr = Address.objects.get(id=addr_id)
        except Exception as e:
            return JsonResponse({'res': 3, 'errmsg': '无效地址'})

        # todo：创建订单核心业务
        # 组织参数
        # 订单id：年月日时分秒+用户id
        order_id = datetime.now().strftime('%Y%m%d%H%M%S')+str(user.id)

        # 运费
        transit_price = 10

        # 总数目和总金额
        total_count = 0
        total_price = 0

        # 设置保存点
        save_id = transaction.savepoint()
        try:
            # todo: 向 df_order_info 表中添加一条记录
            order = OrderInfo.objects.create(
                order_id=order_id,
                user=user,
                address=addr,
                pay_method=pay_method,
                total_count=total_count,
                total_price=total_price,
                transit_price=transit_price)

            # todo：向 df_order_goods 表中添加记录
            conn = get_redis_connection('defacult')
            cart_key = 'cart_{0}'.format(user.id)

            sku_ids = sku_ids.split(',')
            for sku_id in sku_ids:
                # 获取商品信息
                try:
                    # 添加悲观锁
                    # select * from df_goods_sku where id = sku_id for update;
                    sku = GoodsSKU.objects.select_for_update().get(id=sku_id)
                except Exception as e:
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'res': 4, 'errmsg': '商品不存在'})

                # 从 redis 中获取商品的数量
                count = conn.hget(cart_key,sku_id)

                # todo: 判断某一个商品的库存
                if int(count) > sku.stock:
                    transaction.savepoint_rollback(save_id)
                    return JsonResponse({'res': 6, 'errmsg': '商品库存不足'})

                # todo：向 df_order_goods 表中添加一条记录
                OrderGoods.objects.create(
                    order=order,
                    sku=sku,
                    count=count,
                    price=sku.price
                )

                # todo：更新商品的库存和销量
                sku.stock -= int(count)
                sku.sales += int(count)
                sku.save()

                # todo: 累加计算订单商品的总数量和总价格
                amount = sku.price * int(count)
                total_count += int(count)
                total_price += amount

            # todo: 更新订单信息表中的商品的总数量和总价格
            order.total_price = total_price
            order.total_count = total_count
            order.save()
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'res': 7, 'errmsg': '下单失败'})

        # 提交事务
        transaction.savepoint_commit(save_id)

        # todo：清楚用户车中对应的记录
        conn.hget(cart_key,*sku_ids)

        # 返回应答
        return JsonResponse({'res': 5, 'message': '创建成功'})


# 乐观锁
class OrderCommitView1(View):
    """订单创建"""
    @transaction.atomic
    def post(self,request):
        """订单创建"""

        # 判断用户登录
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登陆'})

        # 接受参数
        addr_id = request.POST.get('addr_id')
        pay_method = request.POST.get('pay_method')
        sku_ids = request.POST.get('sku_ids')

        # 校验参数
        if not all([addr_id,pay_method,sku_ids]):
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        # 校验方式支付
        if pay_method not in OrderInfo.PAY_METHOD.keys():
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        # 校验地址
        try:
            addr = Address.objects.get(id=addr_id)
        except Exception as e:
            return JsonResponse({'res': 3, 'errmsg': '无效地址'})

        # todo：创建订单核心业务
        # 组织参加
        # 订单id：年月日时分秒+用户id
        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)

        # 运费
        transit_price = 10

        # 总数目和总金额
        total_count = 0
        total_price = 0

        # 设置保存点
        save_id = transaction.savepoint()

        try:
            # todo：向 df_order_info 表中添加一条记录
            order = OrderInfo.objects.create(
                order_id = order_id,
                user=user,
                address=addr,
                pay_method=pay_method,
                total_count=total_count,
                total_price=total_price,
                transit_price=transit_price
            )

            # todo：向 df_order_goods 表中添加记录
            conn = get_redis_connection('default')
            cart_key = 'cart_{0}'.format(user.id)

            sku_ids = sku_ids.split(',')
            for sku_id in sku_ids:
                # 使用乐观锁，需要重复几次，需要数据库的隔离级别为：提交读 Read commited.
                for i in range(3):
                    # 获取商品信息
                    try:
                        sku = GoodsSKU.objects.get(id=sku_id)
                    except Exception as e:
                        transaction.savepoint_rollback(save_id)
                        return JsonResponse({'res': 4, 'errmsg': '商品不存在'})

                    # 从 redis 中获取商品的数量
                    count = conn.hget(cart_key,sku_id)

                    # todo：判断某一个商品的库存
                    if int(count) > sku.stock:
                        transaction.savepoint_rollback(save_id)
                        return JsonResponse({'res': 6, 'errmsg': '商品库存不足'})

                    # todo：更新商品 的库存和销量
                    orgin_stock = sku.stock
                    orgin_sales = sku.sales
                    new_stock = orgin_stock - int(count)
                    new_sales = orgin_sales + int(count)

                    # 加乐观锁
                    # update df_goods_sku set stock=new_stock,sales=new_sales
                    # where id = sku_id and stock=orgin_stock;
                    res = GoodsSKU.objects.filter(id=sku_id,stock=orgin_stock).update(stock=new_stock,sales=new_sales)
                    if res == 0:
                        if i == 2:
                            # 尝试的第3次
                            transaction.savepoint_rollback(save_id)
                            return JsonResponse({'res': 7, 'errmsg': '下单失败2'})
                        continue

                    # todo：向 df_order_goods 表中添加一条记录
                    OrderGoods.objects.create(order=order,
                                              sku=sku,
                                              count=count,
                                              price=sku.price)

                    # todo：累加计算订单商品的总数量和总价格
                    amount = sku.price * int(count)
                    total_count += int(count)
                    total_price += amount

                    # 如果成功了，跳出循环
                    break

            # todo: 更新订单希希表中的商品的总数量和总价格
            order.total_price = total_price
            order.total_count = total_count
            order.save()
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return JsonResponse({'res': 7, 'errmsg': '下单失败'})

        # 提交事务
        transaction.savepoint_rollback(save_id)

        # todo：清楚用户库中对应的记录
        conn.hdel(cart_key,*sku_ids)

        # 返回应答
        return JsonResponse({'res': 5, 'message': '创建成功'})


# ajax post
# 订单id：order_id
# /order/pay
class OrderPayView(View):
    '''订单支付'''

    def post(self,request):
        '''订单支付'''
        # 判断用户登录
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登陆'})

        # 接受参数
        order_id = request.POST.get('order_id')

        # 校验参数
        if not order_id:
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        try:
            order = OrderInfo.objects.get(order_id=order_id,
                                          user=user,
                                          pay_method=3,
                                          order_status=1)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '无效的订单id'})

        """
            设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置可以查看AlipayClinetConfig的定义
        """
        alipay_client_config = AlipayClientConfig()
        alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
        alipay_client_config.app_id = '2016100100641374'
        app_private_key = ''
        with open(os.path.join(settings.BASE_DIR, 'apps/order/app_private_key.pem'), 'r') as f:
            for line in f:
                app_private_key += line
        alipay_client_config.app_private_key = app_private_key

        alipay_public_key = ''
        with open(os.path.join(settings.BASE_DIR, 'apps/order/alipay_public_key.pem'), 'r') as f:
            for line in f:
                alipay_public_key += line
        alipay_client_config.alipay_public_key = alipay_public_key
        """
            得到客户端对象。
            注意，一个alipay_client_config对象对应一个DefaultAlipayClient，
            定义DefaultAlipayClient对象后，alipay_client_config不得修改，
            如果想使用不同的配置，请定义不同的DefaultAlipayClient。
            logger参数用于打印日志，不传则不打印，建议传递。
        """
        client = DefaultAlipayClient(alipay_client_config=alipay_client_config,logger=logger)

        total_pay = order.transit_price + order.total_price
        total_pay = round(float(total_pay),2)
        model = AlipayTradePagePayModel()
        model.out_trace_no = order_id
        model.total_amount = total_pay
        model.subject = "天天生鲜{0}".format(order_id)
        model.product_code = "FAST_INSTANT_TRADE_PAY"

        request = AlipayTradePagePayRequest(biz_model=model)
        response = client.page_execute(requests,http_method="GET")
        # 访问支付页面
        return JsonResponse({'res': 3, 'response': response})


# ajax post
# 订单id：order_id
# /order/check
class CheckPayView(View):
    """查看订单支付状态"""
    def post(self,request):
        """查看订单支付状态"""
        # 判断用户登录
        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'res': 0, 'errmsg': '用户未登陆'})

        # 接受参数
        order_id = request.POST.get('order_id')

        # 校验参数
        if not order_id:
            return JsonResponse({'res': 1, 'errmsg': '参数不完整'})

        try:
            order = OrderInfo.objects.get(order_id=order_id,
                                          user=user,
                                          pay_method=3,
                                          order_status=1)
        except OrderInfo.DoesNotExist:
            return JsonResponse({'res': 2, 'errmsg': '无效的订单id'})

        """
        设置配置，包括支付宝网关地址、app_id、应用私钥、支付宝公钥等，其他配置值可以查看AlipayClientConfig的定义。
        """
        alipay_client_config = AlipayClientConfig()
        alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
        alipay_client_config.app_id = '2016100100641374'
        app_private_key = ''
        with open(os.path.join(settings.BASE_DIR, 'apps/order/app_private_key.pem'), 'r') as f:
            for line in f:
                app_private_key += line
        alipay_client_config.app_private_key = app_private_key

        alipay_public_key = ''
        with open(os.path.join(settings.BASE_DIR, 'apps/order/alipay_public_key.pem'), 'r') as f:
            for line in f:
                alipay_public_key += line
        alipay_client_config.alipay_public_key = alipay_public_key
        """
        得到客户端对象。
        注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
        logger参数用于打印日志，不传则不打印，建议传递。
        """

        client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)

        total_pay = order.transit_price + order.total_price
        total_pay = round(float(total_pay), 2)
        model = AlipayTradePagePayModel()
        model.out_trade_no = order_id
        model.total_amount = total_pay
        model.subject = "天天生鲜{0}".format(order_id)
        model.product_code = "FAST_INSTANT_TRADE_PAY"

        while True:
            request = AlipayTradeQueryRequest(biz_model=model)
            response = client.page_execute(request, http_method="GET")
            data = requests.get(response)
            data = json.loads(data.text)
            code = data.get('alipay_trade_query_response').get('code')

            trade_status = data.get('alipay_trade_query_response').get('trade_status')
            print(code, trade_status)

            if code == '10000' and trade_status == 'TRADE_SUCCESS':
                # 支付成功
                # 获取支付宝交易号
                trade_no = data.get('alipay_trade_query_response').get('code')
                # 更新订单状态
                order.trade_no = trade_no
                order.order_status = 4
                order.save()
                # 返回结果
                return JsonResponse({'res': 3, 'message': '支付成功'})

            elif code=='40004' or (code == '10000' and trade_status == 'WAIT_BUYER_PAY'):
                # 等待卖家付款
                import time
                time.sleep(5)
                continue
            else:
                # 支付出错
                return JsonResponse({'res': 4, 'errmsg': '支付失败'})


class CommentView(LoginRequiredMixin, View):
    """订单评论"""
    def get(self, request, order_id):
        """提供订单评论页面"""
        user = request.user

        # 校验参数
        if not order_id:
            return redirect(reverse('user:order'))

        try:
            order = OrderInfo.objects.get(order_id=order_id,
                                          user=user,
                                        )
        except OrderInfo.DoesNotExist:
            return redirect(reverse('user:order'))

        order.status_name = OrderInfo.ORDER_STATUS[str(order.order_status)]

        # 获取订单的商品信息
        order_skus = OrderGoods.objects.filter(order=order)
        for order_sku in order_skus:
            # 计算商品小计
            amount = order_sku.price * order_sku.count
            order_sku.amount = amount

        order.order_skus = order_skus

        return render(request, 'df_order/order_comment.html', {'order': order})

    def post(self, request, order_id):
        """处理评论内容"""
        user = request.user

        # 校验参数
        if not order_id:
            return redirect(reverse('user:order'))

        try:
            order = OrderInfo.objects.get(order_id=order_id,
                                          user=user,
                                          )
        except OrderInfo.DoesNotExist:
            return redirect(reverse('user:order'))

        # 获取评论条数
        total_count = request.POST.get('total_count')
        total_count = int(total_count)

        for i in range(1, total_count+1):
            # 获取评论的商品的id
            sku_id = request.POST.get('sku_{0}'.format(i))

            # 获取评论内容
            content = request.POST.get('content_{0}'.format(i))

            try:
                order_goods = OrderGoods.objects.get(order=order, sku_id=sku_id)
            except OrderGoods.DoesNotExist:
                continue

            order_goods.comment = content
            order_goods.save()

        order.order_status = 5
        order.save()

        return redirect(reverse('user:order', kwargs={'page': 1}))


# Create your views here.

# @islogin
# def order(request):
#     """
#         此函数用户下订单页面展示数据
#         接收购物车页面 GET 方法过来的购物车中物品的id，构造购物车对象供订单使用
#     """
#
#     uid = request.session.get('user_id')
#     user = UserInfo.objects.get(id=uid)
#
#     # 获取勾选的每一个订单对象，构造成 list，作为上下文件传入下单页面
#     orderid = request.GET.getlist('orderid')
#     oderlist = []
#
#     for id in orderid:
#         oderlist.append(CartInfo.objects.get(id=int(id)))
#
#     # 判断用户手机号是否为空，分别做展示
#     if user.ushou == '':
#         ushow = ''
#     else:
#         ushow = user.ushou[0:4] + '****' + user.ushou[-4:]
#
#     # 构造上下文
#     context = {'title': '提交订单', 'page_name': 1, 'orderlist': orderlist,'user': user, 'ureceive_phone': ushou}
#
#
# @transaction.atomic()
# @islogin
# def order_handle(request):
#     # 保存一个事物点
#     tran_id = transaction.savepoint()
#     # 接受购物车编号
#     # g根据 POST 和 session 获取信息
#     # cart_ids = post.get('cart_ids')
#     try:
#         post = request.POST
#         orderlist = post.getlist('id[]')
#         total = post.get('total')
#         address = post.get('address')
#
#         order = OrderInfo()
#         now = datetime.now()
#         uid = request.session.get('user_id')
#         order.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
#         order.user_id=uid
#         order.odate=now
#         order.ototal=Decimal(total)
#         order.oaddress = address
#         order.save()
#
#         # 遍历购物车中提交信息，创建订单详情表
#         for orderid in orderlist:
#             cartinfo = CartInfo.objects.get(id=orderid)
#             good = GoodsInfo.objects.get(cartinfo__id=cartinfo.id)
#
#             # 判断库存是否
#             if int(good.gkucun) >= int(cartinfo.count):
#                 # 库存够，移除购买数量并保存
#                 good.gkucun -= int(cartinfo.count)
#                 good.save()
#
#                 goodinfo = GoodsInfo.objects.get(cartinfo__id=orderid)
#
#                 # 创建订单详情表
#                 detailinfo = OrderDetailInfo()
#                 detailinfo.goods_id = int(goodinfo.id)
#                 detailinfo.order_id = int(order.oid)
#                 detailinfo.price = Decimal(int(goodinfo.gprice))
#                 detailinfo.count = int(cartinfo.count)
#                 detailinfo.save()
#
#                 # 循环删除购物车对象
#                 cartinfo.delete()
#             else:
#                 # 库存不够触发事物回滚
#                 transaction.savepoint_rollback(tran_id)
#                 # 返回 json 供前台提示失败
#                 return JsonResponse({'status':2})
#     except Exception as e:
#         print("===========%s"%e)
#         transaction.savepoint_rollback(tran_id)
#         # 返回 json 供前台提示成功
#     return JsonResponse({'status':1})
#
#
# @transaction.atomic()
# def pay(request,oid):
#     order=OrderInfo.objects.get(oid=oid)
#     order.oIspay=True
#     order.save()
#     context={'order':order}
#     return render(request,'order/pay.html',context)