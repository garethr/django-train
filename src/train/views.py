from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404

from train.models import Article
from tagging.models import Tag
	
def tags(request):
    """
    Displays all tags used on the site
    """
    
    tags = Tag.objects.usage_for_model(Article, counts=True)
    return render_to_response('train/tags.html',{'tags': tags})
    
def tiny(request, id):
    "Provide tiny urls based on ids for articles"

    # get the article or throw a 404
    article = get_object_or_404(Article, id=id, status='live')
    url = article.get_absolute_url()
    # redirect to the relevant
    return HttpResponsePermanentRedirect(url)