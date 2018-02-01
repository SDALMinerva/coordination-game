from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    # add cases
    def play_round(self):
        yield (views.AssignAvatar)
        yield (views.Discuss)
        # yield
        yield (views.Decide)
