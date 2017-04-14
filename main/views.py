from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json

class Discuss(Page):

    def vars_for_template(self):
        group_players = self.group.get_players()

        return {
        'avatars': dict([(p.id, p.get_avatar()) for p in group_players]),
        'neighbors': [p.id for p in group_players],
        'messages': {
            1: 'I will go if [x] number go.',
            },
        'wall': json.dumps(self.player.get_messages()),
        }

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Discuss,
    ResultsWaitPage,
    Results
]
