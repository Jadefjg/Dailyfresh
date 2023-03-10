#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ParticipantInfo import ParticipantInfo


class AlipayCommerceEducateInfoParticipantCertifyModel(object):

    def __init__(self):
        self._apply_note_info = None
        self._extend_info = None
        self._from_code = None
        self._participant_info = None
        self._source_id = None

    @property
    def apply_note_info(self):
        return self._apply_note_info

    @apply_note_info.setter
    def apply_note_info(self, value):
        self._apply_note_info = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def from_code(self):
        return self._from_code

    @from_code.setter
    def from_code(self, value):
        self._from_code = value
    @property
    def participant_info(self):
        return self._participant_info

    @participant_info.setter
    def participant_info(self, value):
        if isinstance(value, list):
            self._participant_info = list()
            for i in value:
                if isinstance(i, ParticipantInfo):
                    self._participant_info.append(i)
                else:
                    self._participant_info.append(ParticipantInfo.from_alipay_dict(i))
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_note_info:
            if hasattr(self.apply_note_info, 'to_alipay_dict'):
                params['apply_note_info'] = self.apply_note_info.to_alipay_dict()
            else:
                params['apply_note_info'] = self.apply_note_info
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.from_code:
            if hasattr(self.from_code, 'to_alipay_dict'):
                params['from_code'] = self.from_code.to_alipay_dict()
            else:
                params['from_code'] = self.from_code
        if self.participant_info:
            if isinstance(self.participant_info, list):
                for i in range(0, len(self.participant_info)):
                    element = self.participant_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.participant_info[i] = element.to_alipay_dict()
            if hasattr(self.participant_info, 'to_alipay_dict'):
                params['participant_info'] = self.participant_info.to_alipay_dict()
            else:
                params['participant_info'] = self.participant_info
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateInfoParticipantCertifyModel()
        if 'apply_note_info' in d:
            o.apply_note_info = d['apply_note_info']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'from_code' in d:
            o.from_code = d['from_code']
        if 'participant_info' in d:
            o.participant_info = d['participant_info']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


