from django import template
from forms.models import Options

register = template.Library()


@register.simple_tag
def get_id(option, question):
    op = ""
    for opt in Options.objects.filter(option=option, question=question):
        op = opt
    id = op.id
    return id
