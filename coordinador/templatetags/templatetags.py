from django import template

register = template.Library()

@register.filter
def range(min,max):
    return range(min, max)