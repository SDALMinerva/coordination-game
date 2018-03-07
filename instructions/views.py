from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    template_name = 'instructions/intro.html'
    
class QuizIntro(Page):
    template_name = 'instructions/QuizIntro.html'
    
class InstructionsPage(Page):
    pass

class TourDiscuss(Page):
    template_name = 'tour/Tour-Discuss.html'
    def vars_for_template(self):            
        if self.session.config['condition_network_knowledge'] == 'global':
            networkDisplay = 'The'
        elif self.session.config['condition_network_knowledge'] == 'local':
            networkDisplay = 'Your' 
        
        return {
            'networkDisplay': networkDisplay,
        }
        
class TourDecide(Page):
    template_name = 'tour/Tour-Decide.html'
    def vars_for_template(self):            
        if self.session.config['condition_network_knowledge'] == 'global':
            networkDisplay = 'The'
        elif self.session.config['condition_network_knowledge'] == 'local':
            networkDisplay = 'Your' 
        
        return {
            'networkDisplay': networkDisplay,
        }

class Quiz(Page):
    form_model = models.Player
    def get_form_fields(self):
        questions = [
        'qa1',
        'qa2',
        'qa3',
        'qb1a',
        'qb1b',
        'qb1c',
        'qb2a',
        'qb2b',
        'qb2c',
        'qb2d',
        'qb3a',
        'qb3b',
        'qb3c',
        'qb3d',
        'qb3e',
        'qb3f',
        ]
        return questions

class Summary(Page):
    template_name = 'instructions/Summary.html'

page_sequence = [
    Intro,
    InstructionsPage,
    TourDiscuss,
    TourDecide,
    QuizIntro,
    Quiz,
    Summary,
]
