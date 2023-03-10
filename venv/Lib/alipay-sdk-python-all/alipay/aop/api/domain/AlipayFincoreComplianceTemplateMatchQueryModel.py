#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateMatchQueryModel(object):

    def __init__(self):
        self._biz_object_def_json = None
        self._source_system_id = None
        self._template_lib_code = None
        self._tenant = None

    @property
    def biz_object_def_json(self):
        return self._biz_object_def_json

    @biz_object_def_json.setter
    def biz_object_def_json(self, value):
        self._biz_object_def_json = value
    @property
    def source_system_id(self):
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, value):
        self._source_system_id = value
    @property
    def template_lib_code(self):
        return self._template_lib_code

    @template_lib_code.setter
    def template_lib_code(self, value):
        self._template_lib_code = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_object_def_json:
            if hasattr(self.biz_object_def_json, 'to_alipay_dict'):
                params['biz_object_def_json'] = self.biz_object_def_json.to_alipay_dict()
            else:
                params['biz_object_def_json'] = self.biz_object_def_json
        if self.source_system_id:
            if hasattr(self.source_system_id, 'to_alipay_dict'):
                params['source_system_id'] = self.source_system_id.to_alipay_dict()
            else:
                params['source_system_id'] = self.source_system_id
        if self.template_lib_code:
            if hasattr(self.template_lib_code, 'to_alipay_dict'):
                params['template_lib_code'] = self.template_lib_code.to_alipay_dict()
            else:
                params['template_lib_code'] = self.template_lib_code
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceTemplateMatchQueryModel()
        if 'biz_object_def_json' in d:
            o.biz_object_def_json = d['biz_object_def_json']
        if 'source_system_id' in d:
            o.source_system_id = d['source_system_id']
        if 'template_lib_code' in d:
            o.template_lib_code = d['template_lib_code']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


