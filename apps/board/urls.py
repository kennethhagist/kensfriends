from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^friends$', views.friends, name="friends"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^register$', views.register, name="register"),
    #url(r'^user/(?P<user_id>\d+)$', views.show, name="show")
    #url(r^user/(?P<user_id>\d+)$/add', views.add)
    #url(r^user/(?P<user_id>\d+)$/delete', views.delete)
]
