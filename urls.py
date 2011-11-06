from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'bg.views.main'),
	                   url(r'^(?i)(?P<color>.+)', 'bg.views.showcolor'),
    # Examples:
    # url(r'^$', 'flickrbackground.views.home', name='home'),
    # url(r'^flickrbackground/', include('flickrbackground.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
