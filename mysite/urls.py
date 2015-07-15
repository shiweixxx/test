from django.conf.urls import include, url
from mysite.view import *

urlpatterns = [
    url(r'^test/$', testconf),
]
