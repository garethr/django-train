from django import template
from settings import DEBUG, GOOGLE_ANALYTICS_KEY

register = template.Library()

@register.inclusion_tag('analytics/_google.html')
def google_analytics():
    """
    Usage::

        {% google_analytics %}

    """
    return {
        'debug': DEBUG,
        'key': GOOGLE_ANALYTICS_KEY
    }