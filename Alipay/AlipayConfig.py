# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

DOMAIN = "http:127.0.0.1:8000"


class Config():
    def __init__(self):
        #合作身份者ID，以2088开头由16位纯数字组成的字符串
        self.partner = "2088911384703264"
        #交易安全检验码，由数字和字母组成的32位字符串
        self.key = "cmlac85mu5qcjcqzh694jxgrk0akg64u"
        #签约支付宝账号或卖家支付宝帐户
        self.seller_id = "2088911384703264"
        #页面跳转同步返回页面文件路径 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
        self.return_url = DOMAIN + "/alipay/return/"
        #服务器通知的页面文件路径 要用 http://格式的完整路径，不允许加?id=123这类自定义参数
        self.notify_url = DOMAIN + "/alipay/notify/"

        #字符编码格式 目前支持 gbk 或 utf-8
        self.input_charset = "utf-8"
        #签名方式 不需修改
        self.sign_type = "MD5"
        #访问模式,根据自己的服务器是否支持ssl访问，若支持请选择https；若不支持请选择http
        self.transport = "http"
        #支付宝网关地址（新）
        self.GATEWAY_NEW = "https://mapi.alipay.com/gateway.do?"