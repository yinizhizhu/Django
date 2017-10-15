from addr_book.views import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', passer_student),
    url(r'^passer_teacher/$', passer_teacher),

    url(r'^register/$', register),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^getpassword/$', getpassword),
    url(r'^updatepassword/$', updatepassword),

    url(r'^AboutUs/$', AboutUs),
    url(r'^ContactUs/$', ContactUs),

    url(r'^lookthrough_teacher/$', lookthrough_teacher), #for teacher
    url(r'^lookone_teacher/$', lookone_teacher),
    url(r'^newpublish_teacher/$', newpublish_teacher),
    url(r'^historypublish_teacher/$', historypublish_teacher),
    url(r'^historyget_teacher/$', historyget_teacher),
    url(r'^praise_teacher/$', praise_teacher),
    url(r'^info_teacher/$', info_teacher),
    url(r'^search_teacher/$', search_teacher),
    url(r'^updateinfo_teacher/$', updateinfo_teacher),
    url(r'^delete/$', delete_teacher),

    url(r'^lookthrough_student/$', lookthrough_student), #for student
    url(r'^lookone_student/$', lookone_student),
    url(r'^newpublish_student/$', newpublish_student),
    url(r'^add_student', add_student),
    url(r'^newone_student/$', newone_student),
    url(r'^newpublishone_student/$', newpublishone_student),
    url(r'^deletecontent_student/$', deletecontent_student),


    url(r'^historypublish_student/$', historypublish_student),
    url(r'^historyget_student/$', historyget_student),
    url(r'^praise_student/$', praise_student),
    url(r'^praise_one_student/$', praise_one_student),
    url(r'^search_student/$', search_student),

    url(r'^getorder_teacher/$', getorder_teacher),
    url(r'^getorder_student/$', getorder_student),
)
