from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('teacher.views', 
	url(r'^teacher/$', 'TeacherList'),
	# url(r'^class/$', 'class.views'),
 #    url(r'^students/$', 'students.views'),
 #    url(r'^compositions/$', 'compositions.views'),
 #    url(r'^assignments/$', 'assignments.views'),
    #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)