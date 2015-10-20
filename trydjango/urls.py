from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

     url(r'^$', 'proj.views.home', name='home'),
     url(r'^contact/$', 'proj.views.contact', name='contact'),
     url(r'^myprofile/$', 'proj.views.myprofile', name='myprofile'),
     url(r'^myprofile/cv/(?P<pk>[0-9]+)/edit/$', 'proj.views.edit_cv', name='edit_cv'),
     url(r'^myprofile/new_cv/$', 'proj.views.new_cv', name='new_cv'),
     url(r'^myprofile/cv/(?P<pk>[0-9]+)/$', 'proj.views.cv_detail'),
     url(r'^base_cv/$', 'proj.views.base_cv', name='base_cv'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)