from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^friends$', views.friends),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^user/(?P<user_id>\d+)$', views.show)
    #url(r^user/(?P<user_id>\d+)$/add', views.add)
    #url(r^user/(?P<user_id>\d+)$/other_users', views.other_users)
]
