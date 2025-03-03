#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SummaryInvoiceBillOpenDTO(object):

    def __init__(self):
        self._bill_no = None
        self._buyer_user_id = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SummaryInvoiceBillOpenDTO()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        return o


