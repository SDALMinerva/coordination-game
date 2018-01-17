from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class InstructionsPage(Page):
    pass

class Quiz(Page):
    pass


page_sequence = [
    InstructionsPage,
    Quiz,
]
