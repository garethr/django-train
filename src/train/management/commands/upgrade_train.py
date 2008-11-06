from django.core.management.base import BaseCommand
from django.contrib.markup.templatetags.markup import textile

from train.models import Article

class Command(BaseCommand):
        
    def handle(self, *args, **options):
        articles = Article.objects.all()
        for article in articles:
            article.html = textile(article.content)
            article.save()