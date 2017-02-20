# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'
import urllib2

from AlipayConfig import Config
from AlipayCore import Core


class Notify():
    # HTTPS支付宝通知路径
    Https_verify_url = "https://www.alipay.com/cooperate/gateway.do?service=notify_verify&"
    # HTTP支付宝通知路径
    Http_verify_url = "http://notify.alipay.com/trade/notify_query.do?"

    # 从配置文件中初始化变量
    # <param name="inputPara">通知返回参数数组</param>
    # <param name="notify_id">通知验证ID</param>
    def __init__(self):
        config = Config()
        # 合作身份者ID
        self.partner = config.partner
        self.seller_id = config.seller_id
        # 交易安全校验码
        self.key = config.key
        self.input_charset = config.input_charset
        # 签名方式
        self.sign_type = config.sign_type
        # 访问模式
        self.transport = config.transport

    # <summary>
    #  验证消息是否是支付宝发出的合法消息
    # </summary>
    # <param name="inputPara">通知返回参数数组</param>
    # <returns>验证结果</returns>
    def Verify(self, response_data, method_type):
        # 验证基本数据
        if method_type == "GET":
            if not self.verify_return_base_data(response_data):
                return False
        elif method_type == "POST":
            if not self.verify_notify_base_data(response_data):
                return False
        # 获取返回回来的待签名数组签名后结果
        mysign = self.get_response_mysign(response_data)
        # 获取是否是支付宝服务器发来的请求的验证结果
        responseTxt = self.verify_source(response_data['notify_id'])

        # 验证
        # verify_source的结果不是true，与服务器设置问题、合作身份者ID、notify_id一分钟失效有关
        # mysign与sign不等，与安全校验码、请求时的参数格式（如：带自定义参数等）、编码格式有关
        if responseTxt and response_data['sign'] == mysign:  # 验证成功
            return True
        else:  # 验证失败
            return False

    # <summary>
    # 获取返回回来的待签名数组签名后结果
    # </summary>
    # <param name="inputPara">通知返回参数数组</param>
    # <returns>签名结果字符串</returns>
    def get_response_mysign(self, inputPara):
        # 过滤空值、sign与sign_type参数
        sPara = Core.FilterPara(inputPara)
        # 获得签名结果
        mysign = Core.BuildMysign(sPara, self.key, self.sign_type, self.input_charset)
        return mysign

    def verify_source(self, notify_id, timeout=120000):
        verify_url = self.Https_verify_url
        verify_url += "partner=" + self.partner + "&notify_id=" + notify_id

        # 获取远程服务器ATN结果，验证是否是支付宝服务器发来的请求
        open_url = urllib2.urlopen(verify_url, timeout=timeout)
        return open_url.read() == 'true'

    def verify_return_base_data(self, data):
        required_keys = ['is_success', 'sign', 'sign_type', 'trade_status', 'notify_id', 'seller_id']
        for key in required_keys:
            if key not in data:
                return False
        if data['is_success'] != 'T' or data['trade_status'] != 'TRADE_SUCCESS' \
                or data['seller_id'] != self.seller_id or data['sign_type'] != self.sign_type:
            return False
        return True

    def verify_notify_base_data(self, data):
        required_keys = ['sign', 'sign_type', 'trade_status', 'notify_id', 'seller_id']
        for key in required_keys:
            if key not in data:
                return False
        if data['trade_status'] != 'TRADE_SUCCESS' \
                or data['seller_id'] != self.seller_id or data['sign_type'] != self.sign_type:
            return False
        return True
