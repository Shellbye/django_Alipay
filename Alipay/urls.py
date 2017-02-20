# -*- coding:utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^return/', views.alipay_return, name="return"),
    url(r'^notify/', views.alipay_notify, name="notify"),
    url(r'^$', views.alipay_get_submit_form, name="get_form"),
]
