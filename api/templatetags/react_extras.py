from django import template
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def react_url(app_name):
    return static('js/{}.js'.format(app_name))
