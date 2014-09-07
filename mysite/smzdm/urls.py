from django.conf.urls import *
from smzdm.views import archive

urlpatterns = patterns('',
	url(r'^$', archive),
	)