from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from movemymusic2 import views

admin.autodiscover()

urlpatterns = patterns('', 
	url(r'^teacher/$', views.teacher),
	url(r'^class/$', views.class),
    url(r'^students/', views.students.),
    url(r'^compositions/', views.compositions),
    url(r'^assignments/', views.assignments),
    url(r'^admin/', include(admin.site.urls)),
)
