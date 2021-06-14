from django import template
from forms.models import Options

register = template.Library()


@register.simple_tag
def vote_count(option,question):
    op = ""
    for opt in Options.objects.filter(option=option,question=question):
        op = opt
    votes = op.votes
    return votes
    
