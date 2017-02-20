from django.conf.urls import url, include

from Alipay import views

urlpatterns = [
    url(r'^alipay/', include('Alipay.urls', namespace="alipay")),
    url(r'^$', views.welcome, name='index'),
]
