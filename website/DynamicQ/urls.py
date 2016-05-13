from django.conf.urls import url
from . import views

urlpatterns = [
	# /DynamicQ/
    url(r'^$', views.index, name='index'),

	# /DynamicQ/1
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name ='detail'),
	
	
]
