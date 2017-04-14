from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Brian J. Goode'

doc = """
Welcome the participant and obtain consent. If consent is not given, then redirect user to an exit page. If consent is given, then allow the user to proceed.
"""


class Constants(BaseConstants):
    name_in_url = 'welcome_consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(widget = widgets.CheckboxInput())
