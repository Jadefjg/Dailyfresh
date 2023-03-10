#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OcrTrainScanInfo(object):

    def __init__(self):
        self._destination = None
        self._invoice_date = None
        self._origin = None
        self._passenger = None
        self._price = None
        self._remark = None
        self._seat_class = None
        self._train_no = None

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        self._destination = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value
    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, value):
        self._passenger = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def seat_class(self):
        return self._seat_class

    @seat_class.setter
    def seat_class(self, value):
        self._seat_class = value
    @property
    def train_no(self):
        return self._train_no

    @train_no.setter
    def train_no(self, value):
        self._train_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.destination:
            if hasattr(self.destination, 'to_alipay_dict'):
                params['destination'] = self.destination.to_alipay_dict()
            else:
                params['destination'] = self.destination
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.origin:
            if hasattr(self.origin, 'to_alipay_dict'):
                params['origin'] = self.origin.to_alipay_dict()
            else:
                params['origin'] = self.origin
        if self.passenger:
            if hasattr(self.passenger, 'to_alipay_dict'):
                params['passenger'] = self.passenger.to_alipay_dict()
            else:
                params['passenger'] = self.passenger
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.seat_class:
            if hasattr(self.seat_class, 'to_alipay_dict'):
                params['seat_class'] = self.seat_class.to_alipay_dict()
            else:
                params['seat_class'] = self.seat_class
        if self.train_no:
            if hasattr(self.train_no, 'to_alipay_dict'):
                params['train_no'] = self.train_no.to_alipay_dict()
            else:
                params['train_no'] = self.train_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OcrTrainScanInfo()
        if 'destination' in d:
            o.destination = d['destination']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'origin' in d:
            o.origin = d['origin']
        if 'passenger' in d:
            o.passenger = d['passenger']
        if 'price' in d:
            o.price = d['price']
        if 'remark' in d:
            o.remark = d['remark']
        if 'seat_class' in d:
            o.seat_class = d['seat_class']
        if 'train_no' in d:
            o.train_no = d['train_no']
        return o


