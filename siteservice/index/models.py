#coding: utf-8
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

ARTICLE_TYPE = (
    ('1', u'通知'),
    ('2', u'新闻')
)

class Articles(models.Model):
    title = models.CharField(u'标题', max_length=200)
    content = UEditorField(u'内容', max_length=2000)
    time = models.DateField(u'发布时间', auto_now_add=True)
    isPublish = models.BooleanField(u'是否发布', default=False)
    article_type = models.CharField(u'文章类型', choices=ARTICLE_TYPE, default="1", max_length=1)
    author = models.CharField(u'作者', max_length=100)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title