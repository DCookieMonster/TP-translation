"""translator_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import static

admin.autodiscover()

urlpatterns = [
    url(r'^code','translator.views.code',name='code'),
    url(r'^$','translator.views.register',name='home'),
    url(r'^upload','translator.views.uploadFile',name='upload'),
    url(r'^translate','translator.views.translate',name='translate'),
    url(r'^getFile','translator.views.GetFile',name='getFile'),
    url(r'^getTranslate','translator.views.get_translated_file',name='getTranslate'),
    url(r'^logout','translator.views.logout_view',name='logout'),
    url(r'^profile','translator.views.profile_page',name='profile'),
    url(r'^contact','translator.views.contact_us',name='contact'),
    url(r'^admin/', include(admin.site.urls)),
]
#
# if settings.DEBUG:
#     urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
