from addr_book.views import *
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lab3sae.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^version/$', version),
    url(r'^$', lookthrough),
    url(r'^delete/$', deletebook),
    url(r'^add/$', addbook),
    url(r'^search/$', searchauthor),
    url(r'^update/$', updateinfo),
    url(r'^info/$', clickontitle),
    url(r'^aboutme/$', aboutme),
    url(r'^contactme/$', contactme),
)
