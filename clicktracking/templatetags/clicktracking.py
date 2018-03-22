from django import template
register = template.Library()
import re
from otree.api import safe_json


@register.inclusion_tag('clicktracking/widget.html', takes_context=True)
def clicktrack(context, *args, **kwargs):
    if 'participant' not in context:
        context['vars_for_clicktracking'] = {}
        return context

    #print("Who made context happen? {}".format(context))
    participant = context['participant']

    channel = 'clicktracking-{}'.format(participant.code)

    # channel name should not contain illegal chars,
    # so that it can be used in JS and URLs
    if not re.match(r'^[a-zA-Z0-9_-]+$', channel):
        raise ValueError(
            "'channel' can only contain ASCII letters, numbers, underscores, and hyphens. "
            "Value given was: {}".format(context['channel']))

    context['channel'] = channel

    vars_for_js = {
        'channel': context['channel'],
        'participant_code': participant.code,
    }

    context['vars_for_clicktracking'] = safe_json(vars_for_js)

    return context
