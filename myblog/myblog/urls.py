from blogs.views import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomePage),
    url(r'^PythonFile/$', PythonFile),
    url(r'^PythonDjango/$', PythonDjango),
    url(r'^PythonMysql/$', PythonMysql),
    url(r'^PythonRE/$', PythonRE),
    url(r'^PythonNumpy/$', PythonNumpy),
    url(r'^PythonMatplotlib/$', PythonMatplotlib),
)
