from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from avatar.models import Avatar

class Registration(Page):
    form_model = models.Player;
    form_fields = ['user_name', 'avatar']
    
    def avatar_error_message(self, value):
        if value == "none":
            return "Please select a profile image."

    def vars_for_template(self):
        return {
            'avatars': [a.src for a in Avatar.objects.all()],
        }

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
        
   pass 


page_sequence = [
    Registration,
    ResultsWaitPage,
    Results
]
