from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    cases = ["yes_consent", "no_consent"]
    
    def play_round(self):
        yield (views.WelcomePage)
        if self.case == "yes_consent":
            yield (views.ConsentPage, {"consent": True})
        if self.case == "no_consent":
            yield (views.ConsentPage, {"consent": False})
        yield (views.Results)
