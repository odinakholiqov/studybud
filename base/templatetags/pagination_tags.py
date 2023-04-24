from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag()
def url_place(request, field, value):
    dict_ = request.Get.copy()
    dict_[field] = value

    return dict_.urlencode()