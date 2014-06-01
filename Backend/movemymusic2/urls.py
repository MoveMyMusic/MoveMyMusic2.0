from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('', 
	url(r'^teacher/$', 'teacher.views'),
	url(r'^class/$', 'class.views'),
    url(r'^students/', 'students.views'),
    url(r'^compositions/', 'compositions.views'),
    url(r'^assignments/', 'assignments.views'),
    url(r'^admin/', include(admin.site.urls)),
)
