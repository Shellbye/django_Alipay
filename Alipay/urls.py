# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^return/', 'Alipay.views.alipay_return', name="return"),
                       url(r'^notify/', 'Alipay.views.alipay_notify', name="notify"),
                       url(r'^$', 'Alipay.views.alipay_get_submit_form', name="get_form"),
                       )