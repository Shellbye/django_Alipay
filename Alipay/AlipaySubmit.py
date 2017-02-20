# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

from AlipayConfig import Config
from AlipayCore import Core


class Submit():
    def __init__(self):
        config = Config()
        # 交易安全校验码
        self.key = config.key
        # 编码格式
        self.input_charset = config.input_charset
        # 签名方式
        self.sign_type = config.sign_type
        # 网关
        self.gateway = config.GATEWAY_NEW

    # 生成要请求给支付宝的参数数组
    # <param name="sParaTemp">请求前的参数dict</param>
    # <returns>要请求的参数List</returns>
    def BuildRequestPara(self, sParaTemp):
        # 过滤签名参数数组
        sPara = Core.FilterPara(sParaTemp)

        # 获得签名结果
        mysign = Core.BuildMysign(sPara, self.key, self.sign_type, self.input_charset)

        # 签名结果与签名方式加入请求提交参数组中
        sPara["sign"] = mysign
        sPara["sign_type"] = self.sign_type
        return sPara

    # 生成要请求给支付宝的参数数组
    # <param name="sParaTemp">请求前的参数数组</param>
    # <returns>要请求的参数数组字符串</returns>
    def BuildRequestParaToString(self, sParaTemp):
        # 待签名请求参数数组
        sPara = self.BuildRequestPara(sParaTemp)

        # 把参数组中所有元素，按照“参数=参数值”的模式用“&”字符拼接成字符串
        strRequestData = Core.CreateLinkString(sPara)
        return strRequestData

    # <summary>
    # 构造提交表单HTML数据
    # </summary>
    # <param name="sParaTemp">请求参数数组</param>
    # <param name="gateway">网关地址</param>
    # <param name="strMethod">提交方式。两个值可选：post、get</param>
    # <param name="strButtonValue">确认按钮显示文字</param>
    # <returns>提交表单HTML文本</returns>
    def BuildRequestFormHtml(self, para_temp, method, button_name):
        # 待请求参数数组
        dicPara = self.BuildRequestPara(para_temp)

        sbHtml = ["<form id='alipay_submit' name='alipaysubmit' action='" + self.gateway +
                  "_input_charset=" + self.input_charset + "' method='" + method.lower() + "'>"]

        for key in dicPara:
            sbHtml.append("<input type='hidden' name='%s' value='%s' />" % (key, dicPara[key].decode('utf8')))

        # submit按钮控件请不要含有name属性
        sbHtml.append("<input type='submit' value='" + button_name + "' style='display:none'></form>")

        sbHtml.append("<script>document.forms['alipaysubmit'].submit()</script>")

        return ''.join(sbHtml)
