from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Ethan Vu'

doc = """
Instructions and quiz for participants.  Explains how the experiment will work.
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    qa1 = models.BooleanField(choices = [(True, 'True'), (False, 'False')])
    qa2 = models.BooleanField(choices = [(True, 'True'), (False, 'False')])
    qa3 = models.BooleanField(choices = [(True, 'True'), (False, 'False')])
    
    qb1a = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb1b = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb1c = models.StringField(choices = ['100 points', '50 points', '0 points'])
    
    qb2a = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb2b = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb2c = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb2d = models.StringField(choices = ['100 points', '50 points', '0 points'])
    
    qb3a = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb3b = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb3c = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb3d = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb3e = models.StringField(choices = ['100 points', '50 points', '0 points'])
    qb3f = models.StringField(choices = ['100 points', '50 points', '0 points'])
