from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from train.models import Article
from tagging.models import Tag
	
def tags(request):
    """
    Displays all tags used on the site
    """
    
    tags = Tag.objects.usage_for_model(Article, counts=True)
    return render_to_response('train/tags.html',{'tags': tags})