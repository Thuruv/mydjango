from django.conf.urls import url

from blood import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addme/$', views.add, name='add'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
