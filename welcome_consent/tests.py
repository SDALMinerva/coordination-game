from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    cases = ["yes_consent", "no_consent"]
    
    def play_round(self):
        yield (pages.WelcomePage)
        if self.case == "yes_consent":
            yield (pages.ConsentPage, {"consent": True})
            assert ("Thank you for choosing to participate in our study! If "
                    "at any point in the study you choose to leave, you may do "
                    "so without consequence.") in self.html
            yield (pages.Results)
        if self.case == "no_consent":
            yield (pages.ConsentPage, {"consent": False})
            assert ("Thank you for considering our study, and we are sorry "
                    "to see that you have opted out. Please click next to "
                    "exit.") in self.html
            yield (pages.Results)
