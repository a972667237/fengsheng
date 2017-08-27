from django.shortcuts import render, get_object_or_404, HttpResponse, Http404, HttpResponseRedirect
from .models import Articles
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def index_render(requests):
    host = requests.get_host()
    if host == "www.dsgjjy.com" or host == "dsgjjy.com":
        return HttpResponseRedirect("/ds")
    if host == 'www.bashaman.cn' or host == 'bashaman.cn':
        return render(requests, "inLand/index.html")
    articles_notice = Articles.objects.filter(article_type='1', isPublish=True).order_by("-time")[:5]
    articles_new = Articles.objects.filter(article_type='2', isPublish=True).order_by("-time")[:5]
    return render(requests, 'fengsheng/index.html', locals())

def article_render(requests):
    a_id = requests.GET.get('article_id')
    article = get_object_or_404(Articles, pk=a_id)
    return render(requests, 'fengsheng/article.html', locals())

def list_render(requests):
    list_type = requests.GET.get('list_type', '1')  # 1 or 2 , 1 is notices and the 2 is .........news
    articles = Articles.objects.filter(article_type=list_type, isPublish=True).order_by("-time")
    if not articles:
        raise Http404
    paginator = Paginator(articles, 10)
    page = requests.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(requests, 'fengsheng/articleList.html', locals())

def inland_render(requests):
    return render(requests, "inLand/index.html")