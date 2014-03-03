from django.conf.urls import patterns, include, url
from TranslatorManager import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Translator.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^clients/', views.clients, name='clients'),
    url(r'^jobs/', views.jobs, name='jobs'),
    url(r'^completed/', views.completed, name='completed'),
    #url(r'^jobs/(?P<client>[-\w]+)/all_clients/$', 'all_clients'),
    url(r'^add_client/$', views.add_client, name='add_client'),
    url(r'^add_job/$', views.add_job, name='add_job'),


)
