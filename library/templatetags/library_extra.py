from django import template
import math

register = template.Library()

@register.simple_tag()
def star_rating(rating):
    print(rating)
    out = ""
    for i in range(math.floor(rating)):
        out += '<span class="fa fa-star" checked></span>'
    for i in range(5-math.floor(rating)):
        out += '<span class="fa fa-star"></span>'
    return out
# use django-compont from pip