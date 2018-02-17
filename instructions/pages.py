from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsPage(Page):
    pass

class Quiz(Page):
    form_model = 'player'
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


page_sequence = [
    InstructionsPage,
    Quiz,
]
