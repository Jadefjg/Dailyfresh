#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LinksTemplateData(object):

    def __init__(self):
        self._desc = None
        self._image = None
        self._link = None
        self._title = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.image:
            if hasattr(self.image, 'to_alipay_dict'):
                params['image'] = self.image.to_alipay_dict()
            else:
                params['image'] = self.image
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinksTemplateData()
        if 'desc' in d:
            o.desc = d['desc']
        if 'image' in d:
            o.image = d['image']
        if 'link' in d:
            o.link = d['link']
        if 'title' in d:
            o.title = d['title']
        return o


