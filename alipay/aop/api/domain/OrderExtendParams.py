#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderExtendParams(object):

    def __init__(self):
        self._out_scene_biz_no = None

    @property
    def out_scene_biz_no(self):
        return self._out_scene_biz_no

    @out_scene_biz_no.setter
    def out_scene_biz_no(self, value):
        self._out_scene_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_scene_biz_no:
            if hasattr(self.out_scene_biz_no, 'to_alipay_dict'):
                params['out_scene_biz_no'] = self.out_scene_biz_no.to_alipay_dict()
            else:
                params['out_scene_biz_no'] = self.out_scene_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderExtendParams()
        if 'out_scene_biz_no' in d:
            o.out_scene_biz_no = d['out_scene_biz_no']
        return o


