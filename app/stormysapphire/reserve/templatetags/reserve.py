# -*- encoding: utf-8 -*-
from django import template

register = template.Library()

JP_WEEKDAYS = [u'月', u'火', u'水', u'木', u'金', u'土', u'日']

@register.filter
def jp_weekday(value):
    return JP_WEEKDAYS[value.weekday()]
