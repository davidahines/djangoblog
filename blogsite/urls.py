from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'blogsite.views.home', name='home'),
    #url(r'.*', include('blogengine.urls')),
    url(r'', include('blogengine.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
