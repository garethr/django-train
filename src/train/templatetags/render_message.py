from django import template

register = template.Library()

@register.inclusion_tag('train/_message.html')
def render_message(message):
    """
    Render an message view.

    Usage::

        {% render_message [string] %}

    """
    return {
        'message': message,
    }