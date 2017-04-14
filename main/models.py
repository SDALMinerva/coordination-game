from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Brian J. Goode'

doc = """
Main Coordination Game
"""


class Constants(BaseConstants):
    name_in_url = 'main'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            wall = Wall.objects.create(owner = p)
            wall.message_set.add(
                Message(createdBy=p, 
                        message='Hi, Player {}!'.format(p.id_in_group)
                )
            )

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    def get_messages(self):
        wall = self.wall_set.first()
        wall_messages = wall.message_set.all()

        wall_out = [m.to_dict() for m in wall_messages]

        return wall_out

    def get_avatar(self):
        own_players = self.participant.get_players()
        p_dict = dict([(p.subsession.app_name, p) for p in own_players])

        reg_player = p_dict['registration']
        avatar = reg_player.avatar

        return avatar

class Wall(models.Model):
    owner = models.ForeignKey(Player)

class Message(models.Model):
    wall = models.ForeignKey(Wall)
    createdBy = models.ForeignKey(Player)
    datetime = models.DateTimeField(auto_now=True)
    message = models.CharField()

    def to_dict(self):
        return {
            'timestamp': self.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'content': self.message,
            'author': 'Player {}'.format(self.createdBy_id)
            } 
