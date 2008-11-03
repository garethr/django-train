from django import template

register = template.Library()

@register.inclusion_tag('train/_article.html')
def render_article(article):
    """
    Render an article view.

    Usage::

        {% render_article [article] %}

    """
    return {
        'article': article,
    }
    
@register.inclusion_tag('train/_link.html')
def render_link(article):
    """
    Render an link view.

    Usage::

        {% render_link [article] %}

    """
    return {
        'article': article,
    }