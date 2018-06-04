from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    template_name = 'instructions/intro.html'
    
class QuizIntro(Page):
    template_name = 'instructions/QuizIntro.html'
    
class InstructionsPage(Page):
    def vars_for_template(self):
        comm_type = self.session.config['condition_messaging']
        network_type = self.session.config['condition_network_knowledge']
        screenImage = 'instructions/screenshot-{}-{}.png'
        return {
            'screenImage': screenImage.format(comm_type,network_type)
        }

class TourDiscuss(Page):
    template_name = 'tour/Tour-Discuss.html'

    def is_displayed(self):
        return (self.subsession.session.config['condition_messaging'] != 'none')    
    
    def vars_for_template(self):            
        if self.session.config['condition_network_knowledge'] == 'global':
            networkDisplay = 'The'
        elif self.session.config['condition_network_knowledge'] == 'local':
            networkDisplay = 'Your' 
        
        return {
            'networkDisplay': networkDisplay,
            'group': {
                'Cow': 'Cow-icon.png',
                'Turtle': 'Turtle-icon.png',
                'Cat': 'Cat-icon.png',
                'Swan': 'Swan-icon.png',
                'Eagle': 'Eagle-icon.png',
            }
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
            'group': {
                'Cow': 'Cow-icon.png',
                'Turtle': 'Turtle-icon.png',
                'Cat': 'Cat-icon.png',
                'Swan': 'Swan-icon.png',
                'Eagle': 'Eagle-icon.png',
            }
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
#    Intro,
    InstructionsPage,
    Quiz,
    TourDiscuss,
    TourDecide,
#    QuizIntro,
    Summary,
]
