import datetime

from django.test import TestCase
from django.template import Context, Template

from train.models import Article


class Train(TestCase):
    
    tag_libraries = ['render_article','render_tag_list','render_message',]
    
    def setUp(self):
        article1 = Article(
            title='Title',
            content='Content',
            slug='title',
            tags='tag1, tag2',
            article_type='article',
            status='live',
            pub_date=datetime.datetime(2008, 7, 2, 2, 38, 49)
        )
        article2 = Article(
            title='Title2',
            content='Content2',
            slug='title2',
            tags='tag1, tag3',
            article_type='article',
            status='live',
            pub_date=datetime.datetime(2008, 7, 1, 2, 38, 49)
        )
        article3 = Article(
            title='Title3',
            content='Content3',
            slug='title3',
            tags='tag2',
            article_type='elsewhere',
            status='live',
            pub_date=datetime.datetime(2008, 7, 1, 2, 38, 49)
        )
        article4 = Article(
            title='Title4',
            content='Content4',
            slug='title4',
            tags='',
            article_type='elsewhere',
            status='draft',
            pub_date=datetime.datetime(2008, 7, 1, 2, 38, 49)
        )
        article1.save()
        article2.save()
        article3.save()
        article4.save()
        self.articles = Article.objects.all()
        
    def tearDown(self):
        Article.objects.all().delete()
        
    def assert_contains(self, needle, haystack):
        return self.assert_(needle in haystack, "Content should contain `%s' but doesn't:\n%s" % (needle, haystack))

    def assert_doesnt_contain(self, needle, haystack):
        return self.assert_(needle not in haystack, "Content should not contain `%s' but does:\n%s" % (needle, haystack))

    def assert_equal(self, *args, **kwargs):
        return self.assertEqual(*args, **kwargs)

    def assert_not_equal(self, *args, **kwargs):
        return not self.assertEqual(*args, **kwargs)

    def assert_render(self, expected, template, **kwargs):
        self.assert_equal(expected, self.render(template, **kwargs))

    def assert_doesnt_render(self, expected, template, **kwargs):
        self.assert_not_equal(expected, self.render(template, **kwargs))

    def assert_render_contains(self, expected, template, **kwargs):
        self.assert_contains(expected, self.render(template, **kwargs))

    def assert_render_doesnt_contain(self, expected, template, **kwargs):
        self.assert_doesnt_contain(expected, self.render(template, **kwargs))

    def render(self, template, **kwargs):
        template = "".join(["{%% load %s %%}" % lib for lib in self.tag_libraries]) + template
        return Template(template).render(Context(kwargs)).strip()
        
    def assert_is_instance(self, cls, obj, msg=None):
        if not msg: msg = "%s should be instance of %s" % (obj, cls)
        self.assert_(isinstance(obj, cls), msg)

    def assert_count(self, expected, model):
        actual = model.objects.count()
        self.assert_equal(expected, actual, "%s should have %d objects, had %d" % (model.__name__, expected, actual))

    def assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

