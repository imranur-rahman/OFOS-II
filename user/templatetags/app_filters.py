from django import template
from datetime import date, timedelta

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg


@register.filter(name='add')
def add(value, arg):
    return value + arg