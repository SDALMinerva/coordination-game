from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Results(Page):
    def vars_for_template(self):
        return {
            'payoff_currency': self.participant.payoff.to_real_world_currency(self.session),
        }


page_sequence = [
    Results
]
