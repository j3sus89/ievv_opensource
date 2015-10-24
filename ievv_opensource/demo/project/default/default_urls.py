from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()


default_urls = [
    url(r'^superuser/', include(admin.site.urls)),
]
