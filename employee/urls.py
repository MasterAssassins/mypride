from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add_emp, name='addemp'),
    url(r'^(?P<pk>\d+)/edit/$', views.update_emp, name='updateemp'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete_emp, name='deleteemp'),
]