#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerbaseinfoCreateModel(object):

    def __init__(self):
        self._app_alias_name = None
        self._app_category_ids = None
        self._app_desc = None
        self._app_english_name = None
        self._app_key = None
        self._app_logo = None
        self._app_name = None
        self._app_origin = None
        self._app_slogan = None
        self._app_sub_type = None
        self._app_type = None
        self._client_type = None
        self._inst_code = None
        self._mini_app_id = None
        self._mini_category_ids = None
        self._owner_entity = None
        self._partner_domain = None
        self._pid = None
        self._service_mail = None
        self._service_phone = None

    @property
    def app_alias_name(self):
        return self._app_alias_name

    @app_alias_name.setter
    def app_alias_name(self, value):
        self._app_alias_name = value
    @property
    def app_category_ids(self):
        return self._app_category_ids

    @app_category_ids.setter
    def app_category_ids(self, value):
        self._app_category_ids = value
    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_english_name(self):
        return self._app_english_name

    @app_english_name.setter
    def app_english_name(self, value):
        self._app_english_name = value
    @property
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def app_sub_type(self):
        return self._app_sub_type

    @app_sub_type.setter
    def app_sub_type(self, value):
        self._app_sub_type = value
    @property
    def app_type(self):
        return self._app_type

    @app_type.setter
    def app_type(self, value):
        self._app_type = value
    @property
    def client_type(self):
        return self._client_type

    @client_type.setter
    def client_type(self, value):
        self._client_type = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_category_ids(self):
        return self._mini_category_ids

    @mini_category_ids.setter
    def mini_category_ids(self, value):
        self._mini_category_ids = value
    @property
    def owner_entity(self):
        return self._owner_entity

    @owner_entity.setter
    def owner_entity(self, value):
        self._owner_entity = value
    @property
    def partner_domain(self):
        return self._partner_domain

    @partner_domain.setter
    def partner_domain(self, value):
        self._partner_domain = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def service_mail(self):
        return self._service_mail

    @service_mail.setter
    def service_mail(self, value):
        self._service_mail = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_alias_name:
            if hasattr(self.app_alias_name, 'to_alipay_dict'):
                params['app_alias_name'] = self.app_alias_name.to_alipay_dict()
            else:
                params['app_alias_name'] = self.app_alias_name
        if self.app_category_ids:
            if hasattr(self.app_category_ids, 'to_alipay_dict'):
                params['app_category_ids'] = self.app_category_ids.to_alipay_dict()
            else:
                params['app_category_ids'] = self.app_category_ids
        if self.app_desc:
            if hasattr(self.app_desc, 'to_alipay_dict'):
                params['app_desc'] = self.app_desc.to_alipay_dict()
            else:
                params['app_desc'] = self.app_desc
        if self.app_english_name:
            if hasattr(self.app_english_name, 'to_alipay_dict'):
                params['app_english_name'] = self.app_english_name.to_alipay_dict()
            else:
                params['app_english_name'] = self.app_english_name
        if self.app_key:
            if hasattr(self.app_key, 'to_alipay_dict'):
                params['app_key'] = self.app_key.to_alipay_dict()
            else:
                params['app_key'] = self.app_key
        if self.app_logo:
            if hasattr(self.app_logo, 'to_alipay_dict'):
                params['app_logo'] = self.app_logo.to_alipay_dict()
            else:
                params['app_logo'] = self.app_logo
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.app_slogan:
            if hasattr(self.app_slogan, 'to_alipay_dict'):
                params['app_slogan'] = self.app_slogan.to_alipay_dict()
            else:
                params['app_slogan'] = self.app_slogan
        if self.app_sub_type:
            if hasattr(self.app_sub_type, 'to_alipay_dict'):
                params['app_sub_type'] = self.app_sub_type.to_alipay_dict()
            else:
                params['app_sub_type'] = self.app_sub_type
        if self.app_type:
            if hasattr(self.app_type, 'to_alipay_dict'):
                params['app_type'] = self.app_type.to_alipay_dict()
            else:
                params['app_type'] = self.app_type
        if self.client_type:
            if hasattr(self.client_type, 'to_alipay_dict'):
                params['client_type'] = self.client_type.to_alipay_dict()
            else:
                params['client_type'] = self.client_type
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_category_ids:
            if hasattr(self.mini_category_ids, 'to_alipay_dict'):
                params['mini_category_ids'] = self.mini_category_ids.to_alipay_dict()
            else:
                params['mini_category_ids'] = self.mini_category_ids
        if self.owner_entity:
            if hasattr(self.owner_entity, 'to_alipay_dict'):
                params['owner_entity'] = self.owner_entity.to_alipay_dict()
            else:
                params['owner_entity'] = self.owner_entity
        if self.partner_domain:
            if hasattr(self.partner_domain, 'to_alipay_dict'):
                params['partner_domain'] = self.partner_domain.to_alipay_dict()
            else:
                params['partner_domain'] = self.partner_domain
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.service_mail:
            if hasattr(self.service_mail, 'to_alipay_dict'):
                params['service_mail'] = self.service_mail.to_alipay_dict()
            else:
                params['service_mail'] = self.service_mail
        if self.service_phone:
            if hasattr(self.service_phone, 'to_alipay_dict'):
                params['service_phone'] = self.service_phone.to_alipay_dict()
            else:
                params['service_phone'] = self.service_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerbaseinfoCreateModel()
        if 'app_alias_name' in d:
            o.app_alias_name = d['app_alias_name']
        if 'app_category_ids' in d:
            o.app_category_ids = d['app_category_ids']
        if 'app_desc' in d:
            o.app_desc = d['app_desc']
        if 'app_english_name' in d:
            o.app_english_name = d['app_english_name']
        if 'app_key' in d:
            o.app_key = d['app_key']
        if 'app_logo' in d:
            o.app_logo = d['app_logo']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'app_slogan' in d:
            o.app_slogan = d['app_slogan']
        if 'app_sub_type' in d:
            o.app_sub_type = d['app_sub_type']
        if 'app_type' in d:
            o.app_type = d['app_type']
        if 'client_type' in d:
            o.client_type = d['client_type']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_category_ids' in d:
            o.mini_category_ids = d['mini_category_ids']
        if 'owner_entity' in d:
            o.owner_entity = d['owner_entity']
        if 'partner_domain' in d:
            o.partner_domain = d['partner_domain']
        if 'pid' in d:
            o.pid = d['pid']
        if 'service_mail' in d:
            o.service_mail = d['service_mail']
        if 'service_phone' in d:
            o.service_phone = d['service_phone']
        return o


