from django import template

register = template.Library()

@register.inclusion_tag('train/_tag_list.html')
def render_tag_list(tag_list):
    """
    Render an list of tags.

    Usage::

        {% render_tag_list [tag_list] %}

    """
    return {
        'tag_list': tag_list,
    }