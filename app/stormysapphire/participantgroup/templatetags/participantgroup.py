from django import template

register = template.Library()


@register.filter
def blank(value): 
    if value is None:
        return ''
    return value
