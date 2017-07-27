from django.conf.urls import url, include
from .views import getInfo


urlpatterns = [
    url(r'getInfo', getInfo),
]