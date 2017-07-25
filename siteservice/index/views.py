from django.shortcuts import render

# Create your views here.

def index_render(requests):
    return render(requests, 'index.html')

def article_render(requests):
    return render(requests, 'article.html')