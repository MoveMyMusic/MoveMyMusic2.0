from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('teacher.views', url(r'^teacher/$', 'teacher'),
	'class.views', url(r'^class/$', 'class'),
    'students.views',url(r'^students/', 'students'),
    'compositions.views', url(r'^compositions/', 'compositions'),
    'assignments.views', url(r'^assignments/', 'assignments'),
    url(r'^admin/', include(admin.site.urls)),
)
