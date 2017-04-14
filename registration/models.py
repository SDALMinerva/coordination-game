from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Brian J. Goode'

doc = """
Allow the user to register and create a user profile.
"""


class Constants(BaseConstants):
    name_in_url = 'registration'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_name = models.CharField()
    avatar = models.CharField()
    pass
