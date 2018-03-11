from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edi-wow/$', views.post, name='index'),
    url(r'^fibonacci/(\d{1,2})/$', views.fibo, name='fibo'),
]
