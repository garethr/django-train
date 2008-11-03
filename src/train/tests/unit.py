from django.test import TestCase
from train.tests.common import Train
from train.models import Article

class Unit(Train):
    pass
        
class ArticleMethods(Unit):
    
    def test_get_absolute_url(self):
        self.assertEquals(self.articles[0].get_absolute_url(),'/2008/07/02/title/')
        self.assertEquals(self.articles[1].get_absolute_url(),'/2008/07/01/title2/')