from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^alipay/', include('Alipay.urls', namespace="alipay")),
                       url(r'^$', 'Alipay.views.welcome', name='index'),
)
