from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movemymusic2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('teacher.urls'))
    url(r'^', include('class.urls'))
    url(r'^', include('students.urls'))
    url(r'^', include('compositions.urls'))
    url(r'^', include('assignments.urls'))
    url(r'^admin/', include(admin.site.urls)),
)
