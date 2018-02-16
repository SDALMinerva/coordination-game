from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Tour(Page):
    template_name = 'tour/Tour.html'
    def vars_for_template(self):            
        if self.session.config['condition_network_knowledge'] == 'global':
            networkDisplay = 'The'
        elif self.session.config['condition_network_knowledge'] == 'local':
            networkDisplay = 'Your' 
        
        return {
            'networkDisplay': networkDisplay,
        }


page_sequence = [
    Tour,
]
