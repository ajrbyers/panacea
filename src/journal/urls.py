from django.conf.urls import url

from journal import views

urlpatterns = [
    url(r'^submit/$', views.submit, name='journal_submit'),
]