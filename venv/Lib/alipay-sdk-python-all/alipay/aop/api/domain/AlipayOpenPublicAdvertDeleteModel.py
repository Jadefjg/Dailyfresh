#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenPublicAdvertDeleteModel(object):

    def __init__(self):
        self._advert_group = None
        self._advert_id = None

    @property
    def advert_group(self):
        return self._advert_group

    @advert_group.setter
    def advert_group(self, value):
        self._advert_group = value
    @property
    def advert_id(self):
        return self._advert_id

    @advert_id.setter
    def advert_id(self, value):
        self._advert_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.advert_group:
            if hasattr(self.advert_group, 'to_alipay_dict'):
                params['advert_group'] = self.advert_group.to_alipay_dict()
            else:
                params['advert_group'] = self.advert_group
        if self.advert_id:
            if hasattr(self.advert_id, 'to_alipay_dict'):
                params['advert_id'] = self.advert_id.to_alipay_dict()
            else:
                params['advert_id'] = self.advert_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicAdvertDeleteModel()
        if 'advert_group' in d:
            o.advert_group = d['advert_group']
        if 'advert_id' in d:
            o.advert_id = d['advert_id']
        return o


