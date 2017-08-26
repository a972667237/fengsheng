"""siteservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.http import HttpResponseRedirect
from django.contrib import admin
from index.views import index_render, article_render, list_render, inland_render
import api.urls as api_urls
import dingsheng.urls as dingsheng_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_render),
    url(r'^article', article_render),
    url(r'^inland', inland_render),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^list', list_render),
    url(r'^api/', include(api_urls)),
    url(r'^ds/', include(dingsheng_urls)),
    url(r'^about', lambda x: HttpResponseRedirect('/article?article_id=1')),
    url(r'^guide', lambda x: HttpResponseRedirect('/article?article_id=2')),
    url(r'^rule', lambda x: HttpResponseRedirect('/article?article_id=3')),
]

from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)