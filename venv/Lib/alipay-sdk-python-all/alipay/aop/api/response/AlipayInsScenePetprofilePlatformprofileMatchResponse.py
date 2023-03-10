#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PetMatchScores import PetMatchScores
from alipay.aop.api.domain.PlatformPetProfile import PlatformPetProfile


class AlipayInsScenePetprofilePlatformprofileMatchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePetprofilePlatformprofileMatchResponse, self).__init__()
        self._match_scores = None
        self._pet_profiles = None

    @property
    def match_scores(self):
        return self._match_scores

    @match_scores.setter
    def match_scores(self, value):
        if isinstance(value, list):
            self._match_scores = list()
            for i in value:
                if isinstance(i, PetMatchScores):
                    self._match_scores.append(i)
                else:
                    self._match_scores.append(PetMatchScores.from_alipay_dict(i))
    @property
    def pet_profiles(self):
        return self._pet_profiles

    @pet_profiles.setter
    def pet_profiles(self, value):
        if isinstance(value, list):
            self._pet_profiles = list()
            for i in value:
                if isinstance(i, PlatformPetProfile):
                    self._pet_profiles.append(i)
                else:
                    self._pet_profiles.append(PlatformPetProfile.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePetprofilePlatformprofileMatchResponse, self).parse_response_content(response_content)
        if 'match_scores' in response:
            self.match_scores = response['match_scores']
        if 'pet_profiles' in response:
            self.pet_profiles = response['pet_profiles']
