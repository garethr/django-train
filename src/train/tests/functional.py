from django.test import TestCase
from django.test.client import Client
from train.tests.common import Train
from train.models import Article

class Functional(Train):
    pass
    
class PresenceOfPages(Functional):

    def test_for_homepage(self):
        response = self.client.get('/')
        self.failUnlessEqual(response.status_code, 200)

    def test_for_articles(self):
        for article in self.articles:     
            if article.status == 'live':
                url = article.get_absolute_url()
                response = self.client.get(url)
                self.failUnlessEqual(response.status_code, 200)

    def test_draft_article_does_not_appear(self):
        for article in self.articles:     
            if article.status == 'draft':
                url = article.get_absolute_url()
                response = self.client.get(url)
                self.failUnlessEqual(response.status_code, 404)
                                
class MarkupTests(Functional):

    def test_for_h1_on_homepage(self):
        response = self.client.get('/')
        self.assertContains(response, "<h1",1)

    def test_meta_keywords(self):
        response = self.client.get('/')
        self.assertContains(response, "<meta name=\"description\" content=\"",1)

    def test_meta_keywords(self):
        response = self.client.get('/')
        self.assertContains(response, "<meta name=\"keywords\" content=\"",1)

    def test_for_doctype(self):
        response = self.client.get('/')
        self.assertContains(response, "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">",1)

    def test_for_h1_on_articles(self):
        for article in self.articles:
            if article.status == 'live':
                url = article.get_absolute_url()
                response = self.client.get(url)
                self.assertContains(response, "<h1",1)
    
class TemplateTests(Functional):

    def test_homepage_uses_right_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "train/home.html")

    def test_articles_use_right_templates(self):
        for article in self.articles:
            if article.status == 'live':
                url = article.get_absolute_url()
                response = self.client.get(url)
                self.assertTemplateUsed(response, "base.html")
                self.assertTemplateUsed(response, "train/article_detail.html")
    
class TagsTests(Functional):
    
    def test_canonical_url_for_tags(self):
        #response = self.client.get('/tags/tag1')
        #self.failUnlessEqual(response.status_code, 301)

        response = self.client.get('/tags/tag1/')
        self.failUnlessEqual(response.status_code, 200)
    
    def test_related_tags(self):
        response = self.client.get('/tags/tag1/')
        self.assert_contains("tag2", response.content)
        self.assert_contains("tag3", response.content)

        response = self.client.get('/tags/tag3/')
        self.assert_contains("tag1", response.content)
        self.assert_doesnt_contain("tag2", response.content)

        response = self.client.get('/tags/tag2/')
        self.assert_contains("tag1", response.content)
        self.assert_doesnt_contain("tag3", response.content)
        
class TemplateTagTests(Functional):
    
    def test_render_article_outputs_class_name(self):
        article = self.articles[0]
        self.assert_render_contains('class="article', "{% render_article article %}", article = article)
        self.assert_render_doesnt_contain('class="link', "{% render_article article %}", article = article)

    def test_render_link_outputs_class_name(self):
        article = self.articles[0]
        self.assert_render_contains('class="article link', "{% render_link article %}", article = article)

    def test_render_article_outputs_correct_article(self):
        article = self.articles[0]
        self.assert_render_contains('Title</a></h2>', "{% render_article article %}", article = article)
        
    def test_render_message_outputs_message(self):
        message = "testing 123"
        self.assert_render_contains(message, "{% render_message message %}", message = message)
        
    def test_render_tag_list_doesnt_render_output_for_empty_list(self):
        self.assert_render_doesnt_contain("<ul", "{% render_tag_list tag_list %}", tag_list = [])

    def test_render_tag_list_doesnt_render_output_for_empty_list(self):
        self.assert_render_doesnt_contain("<ul", "{% render_tag_list tag_list %}", tag_list = [])
        
    def test_render_tag_list_gets_passed_list(self):
        self.assert_render_contains("<ul", "{% render_tag_list tag_list %}", tag_list = ['tag1','tag2',])
        self.assert_render_contains("tag1", "{% render_tag_list tag_list %}", tag_list = ['tag1','tag2',])
        self.assert_render_contains("tag2", "{% render_tag_list tag_list %}", tag_list = ['tag1','tag2',])
        