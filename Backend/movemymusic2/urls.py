from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('', 
	url(r'^teacher/$', 'movemymusic2.views.teacher'),
	url(r'^class/$', 'movemymusic2.views.class'),
    url(r'^students/', 'movemymusic2.views.students'),
    url(r'^compositions/', 'movemymusic2.views.compositions'),
    url(r'^assignments/', 'movemymusic2.views.assignments'),
    #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)