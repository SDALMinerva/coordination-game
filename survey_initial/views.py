from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class SocioDemographic(Page):
    form_model = models.Player
    form_fields = [
        'age',
        'income',
        'sex',
        ]

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    SocioDemographic,
    ResultsWaitPage,
    Results
]
