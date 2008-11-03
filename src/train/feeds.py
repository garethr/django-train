from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed

from train.models import Article
from settings import FEED_TITLE, FEED_URL, FEED_DESCRIPTION, FEED_AUTHOR, FEED_EMAIL

class ArticleFeed(Feed):
    """RSS feed for latest 15 blog articles"""
    title = FEED_TITLE
    link = FEED_URL
    description = FEED_DESCRIPTION
    
    item_author_name = FEED_AUTHOR
    item_author_email = FEED_EMAIL
    item_author_link = FEED_URL
    
    def items(self):
        return Article.objects.all().filter(status='live').order_by('-pub_date')[:15]
    
    def item_pubdate(self,item):
        return item.pub_date
        
class AtomArticleFeed(ArticleFeed):
    """ATOM feed for latest 15 blog articles"""
    feed_type = Atom1Feed
    subtitle = ArticleFeed.description