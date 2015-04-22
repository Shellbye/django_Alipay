# -*- coding:utf-8 -*-
__author__ = 'shellbye.com@gmail.com'

import types
import hashlib


class Core():
    def __init__(self):
        pass

    # 生成签名结果
    # <param name="sArray">要签名的数组</param>
    # <param name="key">安全校验码</param>
    # <param name="sign_type">签名类型</param>
    # <param name="input_charset">编码格式</param>
    # <returns>签名结果字符串</returns>
    @staticmethod
    def BuildMysign(paramDic, key, sign_type, input_charset):
        prestr = Core.CreateLinkString(paramDic)  # 把数组所有元素，按照“参数=参数值”的模式用“&”字符拼接成字符串
        prestr = prestr + key                      # 把拼接后的字符串再与安全校验码直接连接起来
        mysign = Core.Sign(prestr, sign_type, input_charset)    # 把最终的字符串签名，获得签名结果
        return mysign

    # <summary>
    # 除去数组中的空值和签名参数
    # </summary>
    # <param name="dicArrayPre">过滤前的参数组</param>
    # <returns>过滤后的参数组</returns>
    @staticmethod
    def FilterPara(paramDicPre):
        paramDic = {}
        for key in paramDicPre:
            key = Core.smart_str(key)
            value = Core.smart_str(paramDicPre[key])
            if key.lower() not in ('sign', 'sign_type') and value:
                paramDic[key] = value
        return paramDic

    # <summary>
    # 把数组所有元素排序，按照“参数=参数值”的模式用“&”字符拼接成字符串
    # </summary>
    # <param name="sArray">需要拼接的数组</param>
    # <returns>拼接完成以后的字符串</returns>
    @staticmethod
    def CreateLinkString(paramDic):
        paramKeys = paramDic.keys()
        #排序
        paramKeys.sort()
        preList = []
        for key in paramKeys:
            preList.append('%s=%s' % (key, paramDic[key]))
        joined_string = '&'.join(preList)
        return joined_string

    # <summary>
    # 签名字符串
    # </summary>
    # <param name="prestr">需要签名的字符串</param>
    # <param name="sign_type">签名类型,这里支持只MD5</param>
    # <param name="input_charset">编码格式</param>
    # <returns>签名结果</returns>
    @staticmethod
    def Sign(prestr, sign_type, input_charset):
        # prestr = prestr.decode(input_charset)
        if sign_type.upper() == "MD5":
            hash_md5 = hashlib.md5()
            hash_md5.update(prestr)
            result = hash_md5.hexdigest()
        else:
            result = sign_type + u'方式签名尚未开发，清自行添加'
        return result

    @staticmethod
    def smart_str(s, encoding='utf-8', strings_only=False, errors='strict'):
        """
        Returns a bytestring version of 's', encoded as specified in 'encoding'.
        If strings_only is True, don't convert (some) non-string-like objects.
        """
        if strings_only and isinstance(s, (types.NoneType, int)):
            return s
        if not isinstance(s, basestring):
            try:
                return str(s)
            except UnicodeEncodeError:
                if isinstance(s, Exception):
                    # An Exception subclass containing non-ASCII data that doesn't
                    # know how to print itself properly. We shouldn't raise a
                    # further exception.
                    return ' '.join([Core.smart_str(arg, encoding, strings_only, errors) for arg in s])
                return unicode(s).encode(encoding, errors)
        elif isinstance(s, unicode):
            return s.encode(encoding, errors)
        elif s and encoding != 'utf-8':
            return s.decode('utf-8', errors).encode(encoding, errors)
        else:
            return s