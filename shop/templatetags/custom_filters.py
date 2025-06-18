from django import template

register = template.Library()

@register.filter
def split(value, delimiter=","):
    return value.split(delimiter)

@register.filter
def trim(value):
    return value.strip()

@register.filter
def subtract(value, arg):
    try:
        return float(value) - float(arg)
    except (ValueError, TypeError):
        return value

@register.filter(name='split_by')
def split_by(value, arg):
    if not value:
        return []
    return value.split(arg)
