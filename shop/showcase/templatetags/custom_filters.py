from django import template

register = template.Library()

@register.filter(name='multiplication_100')
def customFilter(value):
    multiplication = value * 100
    return multiplication