# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

import urllib2
from xml.etree import ElementTree

from AlipayConfig import Config
from AlipaySubmit import Submit


class Service():
    # 构造函数
    def __init__(self):
        # 从配置文件及入口文件中初始化变量
        config = Config()
        #合作者身份ID
        self.partner = config.partner
        #字符编码格式
        self.input_charset = config.input_charset
        #签约支付宝账号或卖家支付宝帐户
        self.seller_id = config.seller_id
        #页面跳转同步返回页面文件路径
        self.return_url = config.return_url
        #服务器通知的页面文件路径
        self.notify_url = config.notify_url
        #支付宝网关地址（新）
        self.GATEWAY_NEW = config.GATEWAY_NEW

    # 构造即时到帐接口
    # <param name="sParaTemp">请求参数集合</param>
    # <returns>表单提交HTML信息</returns>
    def create_direct_pay_by_user(self, sParaTemp):
        #增加基本配置
        sParaTemp["service"] = "create_direct_pay_by_user"
        sParaTemp["partner"] = self.partner
        sParaTemp["_input_charset"] = self.input_charset
        sParaTemp["seller_id"] = self.seller_id
        sParaTemp["return_url"] = self.return_url
        sParaTemp["notify_url"] = self.notify_url

        #确认按钮显示文字
        strButtonValue = u"确认"

        #构造表单提交HTML数据
        submit = Submit()

        #表单提交HTML数据
        strHtml = submit.BuildRequestFormHtml(sParaTemp, "get", strButtonValue)

        return strHtml

    # 用于防钓鱼，调用接口query_timestamp来获取时间戳的处理函数
    # <returns>时间戳字符串</returns>
    def query_timestamp(self):
        url = self.GATEWAY_NEW + "service=query_timestamp&partner=" + self.partner + \
            "&_input_charset=" + self.input_charset

        #从网络获取encrypt_key
        response = urllib2.urlopen(url).read()
        xml_root = ElementTree.fromstring(response)
        encrypt_key = xml_root.find('response').find('timestamp').find('encrypt_key').text
        return encrypt_key
