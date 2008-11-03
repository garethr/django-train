import datetime
import xmlrpclib

from django.db import models
from django.contrib.sitemaps import ping_google

import tagging
from tagging.models import TagManager
from tagging.fields import TagField

from settings import DEBUG, TECHNORATI_URL, TECHNORATI_PING_SERVER, TECHNORATI_SITE_NAME

class Article(models.Model):
    """
    Represents a blog article.
    """
    
    TYPES=(
        ('article','Article'),
        ('link','Link')
    )
    STATUSES=(
        ('draft','Draft'),
        ('live','Live')
    )
    
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250,null=True,blank=True,help_text=u'Useful for search engines.')
    keywords = models.CharField(max_length=250,null=True,blank=True,help_text=u'Comma seperated keywords.')
    content = models.TextField(help_text=u'Use Textile for formatting.')
    tags = TagField(help_text=u'Separate tags with commas or spaces.')
    pub_date = models.DateTimeField(u'Date posted', default=datetime.datetime.today)
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text=u'Used in the URL. Must be unique for the publication date of the entry.')
    article_type = models.CharField("Type",max_length=10,choices=TYPES,default="article")
    status = models.CharField("Status",max_length=10,choices=STATUSES,default="draft")
    enable_comments = models.BooleanField()
    
    location = models.CharField(max_length=250,null=True,blank=True)
    longitude = models.CharField(max_length=250,null=True,blank=True)
    latitude = models.CharField(max_length=250,null=True,blank=True)
    zoom = models.IntegerField(null=True,blank=True)
    
    def get_absolute_url(self):
	    return "/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d"), self.slug)	    
	        
    def __unicode__(self):
		return self.title
		
    class Meta:
        ordering = ["-pub_date"]
        
    def save(self):
        super(Article, self).save()
        if not DEBUG:
            try:
                ping_google('/sitemap.xml')
            except Exception:
                pass

            try:
                technorati = xmlrpclib.Server(TECHNORATI_PING_SERVER)
                reply = technorati.weblogUpdates.ping(TECHNORATI_SITE_NAME,TECHNORATI_URL)
            except Exception:
                pass