#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherTimeRule import VoucherTimeRule
from alipay.aop.api.domain.VoucherSingleItemInfo import VoucherSingleItemInfo
from alipay.aop.api.domain.PromoInfo import PromoInfo
from alipay.aop.api.domain.VoucherTimeRule import VoucherTimeRule
from alipay.aop.api.domain.VoucherUseScopeInfo import VoucherUseScopeInfo


class VoucherTemplate(object):

    def __init__(self):
        self._available_time_rule = None
        self._date_type = None
        self._expire_time = None
        self._item_info = None
        self._promo_info = None
        self._promo_type = None
        self._send_time = None
        self._template_id = None
        self._threshold_amount = None
        self._unavailable_time_rule = None
        self._use_scope_info = None
        self._voucher_desc = None
        self._voucher_name = None
        self._voucher_quantity = None
        self._voucher_type = None

    @property
    def available_time_rule(self):
        return self._available_time_rule

    @available_time_rule.setter
    def available_time_rule(self, value):
        if isinstance(value, list):
            self._available_time_rule = list()
            for i in value:
                if isinstance(i, VoucherTimeRule):
                    self._available_time_rule.append(i)
                else:
                    self._available_time_rule.append(VoucherTimeRule.from_alipay_dict(i))
    @property
    def date_type(self):
        return self._date_type

    @date_type.setter
    def date_type(self, value):
        self._date_type = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def item_info(self):
        return self._item_info

    @item_info.setter
    def item_info(self, value):
        if isinstance(value, VoucherSingleItemInfo):
            self._item_info = value
        else:
            self._item_info = VoucherSingleItemInfo.from_alipay_dict(value)
    @property
    def promo_info(self):
        return self._promo_info

    @promo_info.setter
    def promo_info(self, value):
        if isinstance(value, PromoInfo):
            self._promo_info = value
        else:
            self._promo_info = PromoInfo.from_alipay_dict(value)
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def send_time(self):
        return self._send_time

    @send_time.setter
    def send_time(self, value):
        self._send_time = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value
    @property
    def unavailable_time_rule(self):
        return self._unavailable_time_rule

    @unavailable_time_rule.setter
    def unavailable_time_rule(self, value):
        if isinstance(value, list):
            self._unavailable_time_rule = list()
            for i in value:
                if isinstance(i, VoucherTimeRule):
                    self._unavailable_time_rule.append(i)
                else:
                    self._unavailable_time_rule.append(VoucherTimeRule.from_alipay_dict(i))
    @property
    def use_scope_info(self):
        return self._use_scope_info

    @use_scope_info.setter
    def use_scope_info(self, value):
        if isinstance(value, VoucherUseScopeInfo):
            self._use_scope_info = value
        else:
            self._use_scope_info = VoucherUseScopeInfo.from_alipay_dict(value)
    @property
    def voucher_desc(self):
        return self._voucher_desc

    @voucher_desc.setter
    def voucher_desc(self, value):
        self._voucher_desc = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_quantity(self):
        return self._voucher_quantity

    @voucher_quantity.setter
    def voucher_quantity(self, value):
        self._voucher_quantity = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_time_rule:
            if isinstance(self.available_time_rule, list):
                for i in range(0, len(self.available_time_rule)):
                    element = self.available_time_rule[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_time_rule[i] = element.to_alipay_dict()
            if hasattr(self.available_time_rule, 'to_alipay_dict'):
                params['available_time_rule'] = self.available_time_rule.to_alipay_dict()
            else:
                params['available_time_rule'] = self.available_time_rule
        if self.date_type:
            if hasattr(self.date_type, 'to_alipay_dict'):
                params['date_type'] = self.date_type.to_alipay_dict()
            else:
                params['date_type'] = self.date_type
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.item_info:
            if hasattr(self.item_info, 'to_alipay_dict'):
                params['item_info'] = self.item_info.to_alipay_dict()
            else:
                params['item_info'] = self.item_info
        if self.promo_info:
            if hasattr(self.promo_info, 'to_alipay_dict'):
                params['promo_info'] = self.promo_info.to_alipay_dict()
            else:
                params['promo_info'] = self.promo_info
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.send_time:
            if hasattr(self.send_time, 'to_alipay_dict'):
                params['send_time'] = self.send_time.to_alipay_dict()
            else:
                params['send_time'] = self.send_time
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        if self.unavailable_time_rule:
            if isinstance(self.unavailable_time_rule, list):
                for i in range(0, len(self.unavailable_time_rule)):
                    element = self.unavailable_time_rule[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.unavailable_time_rule[i] = element.to_alipay_dict()
            if hasattr(self.unavailable_time_rule, 'to_alipay_dict'):
                params['unavailable_time_rule'] = self.unavailable_time_rule.to_alipay_dict()
            else:
                params['unavailable_time_rule'] = self.unavailable_time_rule
        if self.use_scope_info:
            if hasattr(self.use_scope_info, 'to_alipay_dict'):
                params['use_scope_info'] = self.use_scope_info.to_alipay_dict()
            else:
                params['use_scope_info'] = self.use_scope_info
        if self.voucher_desc:
            if hasattr(self.voucher_desc, 'to_alipay_dict'):
                params['voucher_desc'] = self.voucher_desc.to_alipay_dict()
            else:
                params['voucher_desc'] = self.voucher_desc
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_quantity:
            if hasattr(self.voucher_quantity, 'to_alipay_dict'):
                params['voucher_quantity'] = self.voucher_quantity.to_alipay_dict()
            else:
                params['voucher_quantity'] = self.voucher_quantity
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherTemplate()
        if 'available_time_rule' in d:
            o.available_time_rule = d['available_time_rule']
        if 'date_type' in d:
            o.date_type = d['date_type']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'item_info' in d:
            o.item_info = d['item_info']
        if 'promo_info' in d:
            o.promo_info = d['promo_info']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'send_time' in d:
            o.send_time = d['send_time']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        if 'unavailable_time_rule' in d:
            o.unavailable_time_rule = d['unavailable_time_rule']
        if 'use_scope_info' in d:
            o.use_scope_info = d['use_scope_info']
        if 'voucher_desc' in d:
            o.voucher_desc = d['voucher_desc']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_quantity' in d:
            o.voucher_quantity = d['voucher_quantity']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


