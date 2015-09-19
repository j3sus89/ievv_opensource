from django.conf.urls import include, url
from django.contrib import admin

#from ievv_opensource.ievv_opensource_admin.cradmin import CrAdminInstance


admin.autodiscover()


default_urls = [
    url(r'^superuser/', include(admin.site.urls)),
    url(r'^socialauth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'},
        name='ievv_opensource-logout'),
    #url(r'^admin/', include(CrAdminInstance.urls())),
]
