from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from avatar.models import Avatar
from random import randint

author = 'Brian J. Goode'

doc = """
Allow the user to register and create a user profile.
"""


class Constants(BaseConstants):
    name_in_url = 'registration'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        rand_avatars = Avatar.randAvatars()
        for p in self.get_players():
            p.avatar = next(rand_avatars)
            p.user_name = p.avatar.name.split('-')[0]
            
            p.participant.vars['avatar-src'] = p.avatar.src
            p.participant.vars['user-name'] = p.user_name


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    user_name = models.StringField(default = 'Not Assigned')
    avatar = models.ForeignKey(Avatar, default = 1)
    pass
