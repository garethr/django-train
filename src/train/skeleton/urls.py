from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

from train.feeds import ArticleFeed, AtomArticleFeed
from train.models import Article

from settings import MEDIA_ROOT

admin.autodiscover()

posts = {
    'queryset': Article.objects.filter(status="live").order_by("-pub_date"),
    'date_field': 'pub_date'
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'blog': GenericSitemap(posts)
}

rss_feeds = {
    'articles': ArticleFeed
}

atom_feeds = {
    'articles': AtomArticleFeed
}

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    ('^admin/(.*)', admin.site.root),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^(?P<url>.*).rss$', 'django.contrib.syndication.views.feed',{'feed_dict':rss_feeds}),
    (r'^(?P<url>.*).atom$', 'django.contrib.syndication.views.feed',{'feed_dict':atom_feeds}),
    ('',include('train.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT,
    }),
)