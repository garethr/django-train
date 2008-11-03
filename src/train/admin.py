from django.contrib import admin
from django import forms
from train.models import Article
from settings import GOOGLE_MAPS_API_KEY

class ArticleOptions(admin.ModelAdmin):
    search_fields = ['title','description','content']
    list_display = ('title','pub_date','article_type','status')
    save_on_top = True
    prepopulated_fields = {'slug': ("title",)}
    ordering = ['-pub_date']
    list_filter = ['article_type','status']
    date_hierarchy = 'pub_date'
    fieldsets = (
        (None,
            {'fields':('title','content','tags','article_type','status','enable_comments')}
        ),
        ('Geo',
            {
                'fields':('location','latitude','longitude','zoom'),
                'classes':('collapse',),                
            }
        ),
        ('Meta',
            {
                'fields':('description','keywords','slug','pub_date'),
                'classes':('collapse',),                
            }
        ),
    )
    class Media:
        googlemaps = "http://maps.google.com/maps?file=api&amp;v=2&amp;key=%s" % GOOGLE_MAPS_API_KEY
        css = { 
        'all': (
				'/assets/css/admin.css',
                ) 
        }
        js = (
				'/assets/js/jquery.js',
				googlemaps,
				'/assets/js/locationpicker.js',
        )

try:
    admin.site.register(Article, ArticleOptions)
except admin.sites.AlreadyRegistered:
    pass