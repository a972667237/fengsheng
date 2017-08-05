from django.conf.urls import url
from .views import index_render, list_render, article_render
from django.http import HttpResponseRedirect

urlpatterns = [
    url('^$', index_render),
    url('^list', list_render),
    url(r'^article', article_render),
    url(r'^about', lambda x: HttpResponseRedirect('/ds/article?article_id=1')),
    url(r'^guide', lambda x: HttpResponseRedirect('/ds/article?article_id=2')),
    url(r'^rule', lambda x: HttpResponseRedirect('/ds/article?article_id=3')),
]