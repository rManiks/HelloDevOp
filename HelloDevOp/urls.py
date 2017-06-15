from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^devop/', include('devop.urls')),
	url(r'^admin/', admin.site.urls),
]

