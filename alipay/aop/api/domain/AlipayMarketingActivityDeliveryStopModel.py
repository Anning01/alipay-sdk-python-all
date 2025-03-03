#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryAgencyMerchantInfo import DeliveryAgencyMerchantInfo
from alipay.aop.api.domain.DeliveryConfig import DeliveryConfig


class AlipayMarketingActivityDeliveryStopModel(object):

    def __init__(self):
        self._belong_merchant_info = None
        self._delivery_config_list = None

    @property
    def belong_merchant_info(self):
        return self._belong_merchant_info

    @belong_merchant_info.setter
    def belong_merchant_info(self, value):
        if isinstance(value, DeliveryAgencyMerchantInfo):
            self._belong_merchant_info = value
        else:
            self._belong_merchant_info = DeliveryAgencyMerchantInfo.from_alipay_dict(value)
    @property
    def delivery_config_list(self):
        return self._delivery_config_list

    @delivery_config_list.setter
    def delivery_config_list(self, value):
        if isinstance(value, list):
            self._delivery_config_list = list()
            for i in value:
                if isinstance(i, DeliveryConfig):
                    self._delivery_config_list.append(i)
                else:
                    self._delivery_config_list.append(DeliveryConfig.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.belong_merchant_info:
            if hasattr(self.belong_merchant_info, 'to_alipay_dict'):
                params['belong_merchant_info'] = self.belong_merchant_info.to_alipay_dict()
            else:
                params['belong_merchant_info'] = self.belong_merchant_info
        if self.delivery_config_list:
            if isinstance(self.delivery_config_list, list):
                for i in range(0, len(self.delivery_config_list)):
                    element = self.delivery_config_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_config_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_config_list, 'to_alipay_dict'):
                params['delivery_config_list'] = self.delivery_config_list.to_alipay_dict()
            else:
                params['delivery_config_list'] = self.delivery_config_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingActivityDeliveryStopModel()
        if 'belong_merchant_info' in d:
            o.belong_merchant_info = d['belong_merchant_info']
        if 'delivery_config_list' in d:
            o.delivery_config_list = d['delivery_config_list']
        return o


