from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve

from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/orcid/$', views.orcid_login, name='orcid_login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^journal/', include('journal.urls'))
]


# Allow Django to serve static content only in debug/dev mode
if settings.DEBUG:

    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^404/$', TemplateView.as_view(template_name='core/404.html')),
        url(r'^500/$', TemplateView.as_view(template_name='core/500.html')),
    ]