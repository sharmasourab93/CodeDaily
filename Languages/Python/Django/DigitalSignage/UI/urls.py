from django.conf.urls import url,include
from . import views
app_name='UI'

urlpatterns = [
    url(r'^login/$',views.IndexView.as_view(),name='index'),
    url(r'^logout/$',views.logout_view,name='logout_view'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^add/$',views.MainDBCreate.as_view(),name='add-row'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.MainDBDelete.as_view(), name='delete-row'),
]
