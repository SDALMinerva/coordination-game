from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):
    # add cases
    def play_round(self):
        yield (views.AssignAvatar)
        
        # Should match the # of 'messaging rounds'
        yield (views.Discuss)
        yield (views.Discuss)
        yield (views.Decide, {'participate': True})
