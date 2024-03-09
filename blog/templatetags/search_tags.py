from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def highlight(value, arg):
    highlighted = value.replace(arg, f'<b style="color: red;">{arg}</b>')
    return mark_safe(highlighted)
