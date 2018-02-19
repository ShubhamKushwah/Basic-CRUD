from django.conf.urls import url
from programmer.views import HomeView, doc_delete, UpdateProgView

urlpatterns = [

    url(r'^$', HomeView.as_view(), name="home"),

    url(r'^(?P<pk>\d+)/delete/$', doc_delete, name='delete'),

    url(r'^(?P<pk>\d+)/update/$', UpdateProgView.as_view(), name='update'),

]