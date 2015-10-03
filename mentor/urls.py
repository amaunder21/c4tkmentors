from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'lostpass', views.lostpass, name='lostpass'),
    url(r'register', views.register, name='register'),
    url(r'success', views.success, name='success'),
    url(r'^$', views.index, name='index'),
]