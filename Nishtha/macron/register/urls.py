from django.conf.urls import url
from register import views

urlpatterns = [
    url(r'^customer/$', views.details),
    url(r'^customer/(?P<phone>[0-9]+)/$', views.CustomerDetail.as_view()),
]
