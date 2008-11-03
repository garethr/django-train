from django.test import TestCase
from train.tests.common import Train
from train.models import Article

class System(Train):
    pass
    
class Articles(System):

    def test_number_of_pages_in_self(self):
        expected = 4
        actual = len(self.articles)
        self.assertEquals(expected,actual,'number of pages in self should be %s, but instead is %s' % (expected,actual))

    def test_number_of_pages(self):
        self.assert_count(4,Article)