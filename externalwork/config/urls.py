from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apps.hello.views import hello


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'externalwork.views.home', name='home'),
    # url(r'^externalwork/', include('externalwork.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns = patterns('',
    url(r'^home/', hello)
)

urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
