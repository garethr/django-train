from django.conf.urls.defaults import *
from django.views.generic import date_based, list_detail

from tagging.views import tagged_object_list

from train.views import tags, tiny
from train.models import Article

post_home = {
    'queryset': Article.objects.filter(status="live").order_by("-pub_date"),
    'template_name' : "train/home.html",
    'paginate_by' : 15
}

posts = {
    'queryset': Article.objects.filter(status="live").order_by("-pub_date"),
    'date_field': 'pub_date'
}

tinyposts = {
    'queryset': Article.objects.filter(status="live").order_by("-pub_date"),
}

urlpatterns = patterns('',
    url(r'^$',
        list_detail.object_list,
        post_home,
        name='train_article_archive_index'),
    url(r'^(?P<id>\d+)$',
        tiny,
        name='train_article_tinyurl'),
    url(r'^(?P<year>\d{4})/$',
        date_based.archive_year,
        dict(posts, make_object_list=True),
        name='train_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        date_based.archive_month,
        dict(posts, month_format='%m'),
        name='train_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',
        date_based.archive_day,
        dict(posts, month_format='%m'),
        name='train_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        date_based.object_detail,
        dict(posts, slug_field='slug', month_format='%m'),
        name='train_entry_detail'),
    (r'^tags/$', tags),
    url(r'^tags/(?P<tag>[^/]+)/$',
        tagged_object_list,
        dict(queryset_or_model=Article, related_tags=True, allow_empty=True),
        name='widget_tag_detail'),
)