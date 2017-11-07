from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json

class Discuss(Page):

    def vars_for_template(self):
        group_players = self.group.get_players()

        return {
        'avatar': self.player.get_avatar(),
        'user_name': self.player.get_user_name(),
        'avatars': dict([(p.id, p.get_avatar()) for p in group_players]),
        'thresholds': dict([(p.id, p.node.threshold_text) for p in group_players]),
        'user_names': dict([(p.id, p.get_user_name()) for p in group_players]),
        'neighbors': [p.id for p in self.player.get_neighbors()],
        'messages': {
            1: 'I will participate.',
            2: 'I will not participate.',
            },
        'wall': json.dumps(self.player.get_messages()),
        'nodes': json.dumps(self.subsession.network.getNodes()),
        'edges': json.dumps(self.subsession.network.getEdges()),
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
