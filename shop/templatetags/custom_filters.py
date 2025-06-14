# shop/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter(name='split_by')
def split_by(value, arg):
    """
    Usage: {{ value|split_by:"," }}
    """
    if not value:
        return []
    return value.split(arg)