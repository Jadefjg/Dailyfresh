#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.constant.ParamConstants import *




class AlipayOpenAgentCommonSignRequest(object):

    def __init__(self, biz_model=None):
        self._biz_model = biz_model
        self._alipay_life_name = None
        self._app_name = None
        self._batch_no = None
        self._business_license_no = None
        self._date_limitation = None
        self._long_term = None
        self._mcc_code = None
        self._product_code = None
        self._web_sites = None
        self._web_status = None
        self._web_test_account = None
        self._web_test_account_password = None
        self._wechat_official_account_name = None
        self._app_demo = None
        self._business_license_auth_pic = None
        self._business_license_pic = None
        self._shop_scene_pic = None
        self._shop_sign_board_pic = None
        self._special_license_pic = None
        self._web_home_screenshot = None
        self._web_item_screenshot = None
        self._web_pay_screenshot = None
        self._web_sites_loa = None
        self._version = "1.0"
        self._terminal_type = None
        self._terminal_info = None
        self._prod_code = None
        self._notify_url = None
        self._return_url = None
        self._udf_params = None
        self._need_encrypt = False

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value

    @property
    def alipay_life_name(self):
        return self._alipay_life_name

    @alipay_life_name.setter
    def alipay_life_name(self, value):
        self._alipay_life_name = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def date_limitation(self):
        return self._date_limitation

    @date_limitation.setter
    def date_limitation(self, value):
        self._date_limitation = value
    @property
    def long_term(self):
        return self._long_term

    @long_term.setter
    def long_term(self, value):
        self._long_term = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def web_sites(self):
        return self._web_sites

    @web_sites.setter
    def web_sites(self, value):
        if isinstance(value, list):
            self._web_sites = list()
            for i in value:
                self._web_sites.append(i)
    @property
    def web_status(self):
        return self._web_status

    @web_status.setter
    def web_status(self, value):
        self._web_status = value
    @property
    def web_test_account(self):
        return self._web_test_account

    @web_test_account.setter
    def web_test_account(self, value):
        self._web_test_account = value
    @property
    def web_test_account_password(self):
        return self._web_test_account_password

    @web_test_account_password.setter
    def web_test_account_password(self, value):
        self._web_test_account_password = value
    @property
    def wechat_official_account_name(self):
        return self._wechat_official_account_name

    @wechat_official_account_name.setter
    def wechat_official_account_name(self, value):
        self._wechat_official_account_name = value

    @property
    def app_demo(self):
        return self._app_demo

    @app_demo.setter
    def app_demo(self, value):
        if not isinstance(value, FileItem):
            return
        self._app_demo = value
    @property
    def business_license_auth_pic(self):
        return self._business_license_auth_pic

    @business_license_auth_pic.setter
    def business_license_auth_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_auth_pic = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._business_license_pic = value
    @property
    def shop_scene_pic(self):
        return self._shop_scene_pic

    @shop_scene_pic.setter
    def shop_scene_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._shop_scene_pic = value
    @property
    def shop_sign_board_pic(self):
        return self._shop_sign_board_pic

    @shop_sign_board_pic.setter
    def shop_sign_board_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._shop_sign_board_pic = value
    @property
    def special_license_pic(self):
        return self._special_license_pic

    @special_license_pic.setter
    def special_license_pic(self, value):
        if not isinstance(value, FileItem):
            return
        self._special_license_pic = value
    @property
    def web_home_screenshot(self):
        return self._web_home_screenshot

    @web_home_screenshot.setter
    def web_home_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._web_home_screenshot = value
    @property
    def web_item_screenshot(self):
        return self._web_item_screenshot

    @web_item_screenshot.setter
    def web_item_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._web_item_screenshot = value
    @property
    def web_pay_screenshot(self):
        return self._web_pay_screenshot

    @web_pay_screenshot.setter
    def web_pay_screenshot(self, value):
        if not isinstance(value, FileItem):
            return
        self._web_pay_screenshot = value
    @property
    def web_sites_loa(self):
        return self._web_sites_loa

    @web_sites_loa.setter
    def web_sites_loa(self, value):
        if not isinstance(value, FileItem):
            return
        self._web_sites_loa = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def terminal_type(self):
        return self._terminal_type

    @terminal_type.setter
    def terminal_type(self, value):
        self._terminal_type = value

    @property
    def terminal_info(self):
        return self._terminal_info

    @terminal_info.setter
    def terminal_info(self, value):
        self._terminal_info = value

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value

    @property
    def notify_url(self):
        return self._notify_url

    @notify_url.setter
    def notify_url(self, value):
        self._notify_url = value

    @property
    def return_url(self):
        return self._return_url

    @return_url.setter
    def return_url(self, value):
        self._return_url = value

    @property
    def udf_params(self):
        return self._udf_params

    @udf_params.setter
    def udf_params(self, value):
        if not isinstance(value, dict):
            return
        self._udf_params = value

    @property
    def need_encrypt(self):
        return self._need_encrypt

    @need_encrypt.setter
    def need_encrypt(self, value):
        self._need_encrypt = value

    def add_other_text_param(self, key, value):
        if not self.udf_params:
            self.udf_params = dict()
        self.udf_params[key] = value

    def get_params(self):
        params = dict()
        params[P_METHOD] = 'alipay.open.agent.common.sign'
        params[P_VERSION] = self.version
        if self.biz_model:
            params[P_BIZ_CONTENT] = json.dumps(obj=self.biz_model.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.alipay_life_name:
            if hasattr(self.alipay_life_name, 'to_alipay_dict'):
                params['alipay_life_name'] = json.dumps(obj=self.alipay_life_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['alipay_life_name'] = self.alipay_life_name
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = json.dumps(obj=self.app_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['app_name'] = self.app_name
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = json.dumps(obj=self.batch_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['batch_no'] = self.batch_no
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = json.dumps(obj=self.business_license_no.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['business_license_no'] = self.business_license_no
        if self.date_limitation:
            if hasattr(self.date_limitation, 'to_alipay_dict'):
                params['date_limitation'] = json.dumps(obj=self.date_limitation.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['date_limitation'] = self.date_limitation
        if self.long_term:
            if hasattr(self.long_term, 'to_alipay_dict'):
                params['long_term'] = json.dumps(obj=self.long_term.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['long_term'] = self.long_term
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = json.dumps(obj=self.mcc_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['mcc_code'] = self.mcc_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = json.dumps(obj=self.product_code.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['product_code'] = self.product_code
        if self.web_sites:
            if isinstance(self.web_sites, list):
                for i in range(0, len(self.web_sites)):
                    element = self.web_sites[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.web_sites[i] = element.to_alipay_dict()
                params['web_sites'] = json.dumps(obj=self.web_sites, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
        if self.web_status:
            if hasattr(self.web_status, 'to_alipay_dict'):
                params['web_status'] = json.dumps(obj=self.web_status.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['web_status'] = self.web_status
        if self.web_test_account:
            if hasattr(self.web_test_account, 'to_alipay_dict'):
                params['web_test_account'] = json.dumps(obj=self.web_test_account.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['web_test_account'] = self.web_test_account
        if self.web_test_account_password:
            if hasattr(self.web_test_account_password, 'to_alipay_dict'):
                params['web_test_account_password'] = json.dumps(obj=self.web_test_account_password.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['web_test_account_password'] = self.web_test_account_password
        if self.wechat_official_account_name:
            if hasattr(self.wechat_official_account_name, 'to_alipay_dict'):
                params['wechat_official_account_name'] = json.dumps(obj=self.wechat_official_account_name.to_alipay_dict(), ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            else:
                params['wechat_official_account_name'] = self.wechat_official_account_name
        if self.terminal_type:
            params['terminal_type'] = self.terminal_type
        if self.terminal_info:
            params['terminal_info'] = self.terminal_info
        if self.prod_code:
            params['prod_code'] = self.prod_code
        if self.notify_url:
            params['notify_url'] = self.notify_url
        if self.return_url:
            params['return_url'] = self.return_url
        if self.udf_params:
            params.update(self.udf_params)
        return params

    def get_multipart_params(self):
        multipart_params = dict()
        if self.app_demo:
            multipart_params['app_demo'] = self.app_demo
        if self.business_license_auth_pic:
            multipart_params['business_license_auth_pic'] = self.business_license_auth_pic
        if self.business_license_pic:
            multipart_params['business_license_pic'] = self.business_license_pic
        if self.shop_scene_pic:
            multipart_params['shop_scene_pic'] = self.shop_scene_pic
        if self.shop_sign_board_pic:
            multipart_params['shop_sign_board_pic'] = self.shop_sign_board_pic
        if self.special_license_pic:
            multipart_params['special_license_pic'] = self.special_license_pic
        if self.web_home_screenshot:
            multipart_params['web_home_screenshot'] = self.web_home_screenshot
        if self.web_item_screenshot:
            multipart_params['web_item_screenshot'] = self.web_item_screenshot
        if self.web_pay_screenshot:
            multipart_params['web_pay_screenshot'] = self.web_pay_screenshot
        if self.web_sites_loa:
            multipart_params['web_sites_loa'] = self.web_sites_loa
        return multipart_params
