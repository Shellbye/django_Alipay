# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'
import time
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from AlipayService import Service
from AlipayNotify import Notify


def welcome(request):
    return HttpResponse("click <a href=" + reverse('alipay:get_form') + ">here</a> to test")


def alipay_get_submit_form(request):
    return HttpResponse(create_the_form())


def create_the_form():
    service = Service()

    out_trade_no = time.time()
    encrypt_key = service.query_timestamp()
    param = {
        "payment_type": 1,
        "out_trade_no": out_trade_no,
        "subject": "商品名称",
        "total_fee": 0.01,
        "body": "body",
        "show_url": "http://shellbye.com/blog/",
        "anti_phishing_key": encrypt_key,
        "exter_invoke_ip": "",
    }
    html = service.create_direct_pay_by_user(param)
    return html


def alipay_return(request):
    notify = Notify()
    if notify.Verify(request.GET, "GET"):
        return HttpResponse("支付成功")
    else:
        return HttpResponse("支付失败")


@csrf_exempt
def alipay_notify(request):
    notify = Notify()
    if notify.Verify(request.POST, "POST"):
        return HttpResponse("success")
    else:
        return HttpResponse("fail")

