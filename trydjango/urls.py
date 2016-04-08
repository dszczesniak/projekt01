from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

     url(r'^$', 'proj.views.home', name='home'),
     url(r'^(?P<pk>[0-9]+)/send_message/$', 'proj.views.send_message', name='send_message'),
   #  url(r'^myprofile/$', 'proj.views.myprofile', name='myprofile'),
     url(r'^cv/(?P<pk>[0-9]+)/edit/$', 'proj.views.edit_cv', name='edit_cv'),
     url(r'^new_cv/$', 'proj.views.new_cv', name='new_cv'),
     url(r'^cv/(?P<pk>[0-9]+)/$', 'proj.views.cv_detail'),
     url(r'^base_cv/$', 'proj.views.base_cv', name='base_cv'),
     url(r'^(?P<pk>[0-9]+)/edit_profile/$', 'proj.views.profile_settings', name='profile_settings'),
     url(r'^(?P<pk>[0-9]+)/update_exp/$', 'proj.views.update_exp', name='update_exp'),
     url(r'^groups/$', 'proj.views.groups', name='groups'),
     url(r'^(?P<pk>[0-9]+)/choose_group/$', 'proj.views.choose_group', name='choose_group'),
     url(r'^(?P<pk>[0-9]+)/skill_settings/$', 'proj.views.skill_settings', name='skill_settings'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^accounts/login/$',  'proj.views.login'),
     url(r'^accounts/auth/$',  'proj.views.auth_view'),
     url(r'^accounts/logout/$',  'proj.views.logout'),
     url(r'^accounts/invalid/$',  'proj.views.invalid_login'),
     url(r'^accounts/register/$',  'proj.views.register_user'),
     url(r'^accounts/register_success/$',  'proj.views.register_success'),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^accounts/', include('registration.backends.default.urls')),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
                    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)