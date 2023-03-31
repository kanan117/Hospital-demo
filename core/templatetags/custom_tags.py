from django import template

from core.models import Blogs

register = template.Library()

@register.simple_tag
def get_blogs(offset, limit):
    return Blogs.objects.filter(is_published=True)[offset:limit]

