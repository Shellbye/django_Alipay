# django_Alipay
An python implementation of Alipay alipaydirect 

# 关于

这是一个基于[前辈](https://code.google.com/p/alipay-python/)的工作成果的
支付宝实时交易接口实现

我用Django搭建了一个简单的框架用于测试。

# 配置

*必需*要用户自己的配置的信息是```Alipay.AlipayConfig```中的如下几行：

    self.partner = "2088xxxxxxxxxxxx"
    #交易安全检验码，由数字和字母组成的32位字符串
    self.key = "abcdefghijklmnopqrstuvwxyz123456"
    #签约支付宝账号或卖家支付宝帐户
    self.seller_id = "2088xxxxxxxxxxxx"

其余部分可以不用配置。

# 使用

为了简化测试（不需要输入任何信息），
我把很多信息都直接写死在了```Alipay.views.create_the_form```。

具体的参数以及各个语言的官方demo在[这里](https://b.alipay.com/newIndex.htm)

测试直接启动项目，访问[http://127.0.0.1:8000/](http://127.0.0.1:8000/)，
然后点击here即可，测试金额是一分钱(0.01RMB)。

# 其他

目前实时到账是测试过了的，其他交易类型因为没有相应权限的账号，所以还没有测试过。