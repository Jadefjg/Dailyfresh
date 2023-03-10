#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PayForPrivilegePaidVoucherConfig import PayForPrivilegePaidVoucherConfig


class PayForPrivilegePromotionPlanInfo(object):

    def __init__(self):
        self._benefit = None
        self._create_time = None
        self._end_time = None
        self._modify_time = None
        self._out_biz_no = None
        self._paid_voucher_list = None
        self._principal = None
        self._promotion_plan_id = None
        self._start_time = None
        self._status = None

    @property
    def benefit(self):
        return self._benefit

    @benefit.setter
    def benefit(self, value):
        self._benefit = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def modify_time(self):
        return self._modify_time

    @modify_time.setter
    def modify_time(self, value):
        self._modify_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def paid_voucher_list(self):
        return self._paid_voucher_list

    @paid_voucher_list.setter
    def paid_voucher_list(self, value):
        if isinstance(value, list):
            self._paid_voucher_list = list()
            for i in value:
                if isinstance(i, PayForPrivilegePaidVoucherConfig):
                    self._paid_voucher_list.append(i)
                else:
                    self._paid_voucher_list.append(PayForPrivilegePaidVoucherConfig.from_alipay_dict(i))
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def promotion_plan_id(self):
        return self._promotion_plan_id

    @promotion_plan_id.setter
    def promotion_plan_id(self, value):
        self._promotion_plan_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit:
            if hasattr(self.benefit, 'to_alipay_dict'):
                params['benefit'] = self.benefit.to_alipay_dict()
            else:
                params['benefit'] = self.benefit
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.modify_time:
            if hasattr(self.modify_time, 'to_alipay_dict'):
                params['modify_time'] = self.modify_time.to_alipay_dict()
            else:
                params['modify_time'] = self.modify_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.paid_voucher_list:
            if isinstance(self.paid_voucher_list, list):
                for i in range(0, len(self.paid_voucher_list)):
                    element = self.paid_voucher_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.paid_voucher_list[i] = element.to_alipay_dict()
            if hasattr(self.paid_voucher_list, 'to_alipay_dict'):
                params['paid_voucher_list'] = self.paid_voucher_list.to_alipay_dict()
            else:
                params['paid_voucher_list'] = self.paid_voucher_list
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.promotion_plan_id:
            if hasattr(self.promotion_plan_id, 'to_alipay_dict'):
                params['promotion_plan_id'] = self.promotion_plan_id.to_alipay_dict()
            else:
                params['promotion_plan_id'] = self.promotion_plan_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayForPrivilegePromotionPlanInfo()
        if 'benefit' in d:
            o.benefit = d['benefit']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'modify_time' in d:
            o.modify_time = d['modify_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'paid_voucher_list' in d:
            o.paid_voucher_list = d['paid_voucher_list']
        if 'principal' in d:
            o.principal = d['principal']
        if 'promotion_plan_id' in d:
            o.promotion_plan_id = d['promotion_plan_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


