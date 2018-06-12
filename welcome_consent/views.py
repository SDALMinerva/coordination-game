from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
    is_debug = False
    pass

class ConsentPage(Page):
    form_model = models.Player
    form_fields = ['consent']
    
    def before_next_page(self):
        self.participant.vars['consent'] = self.player.consent

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Results(Page):
    def is_displayed(self):
        return not self.participant.vars['consent']


page_sequence = [
    WelcomePage,
    ConsentPage,
    Results,
]
