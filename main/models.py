from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from network.models import Network, Edge, Node
from random import randint

author = 'Brian J. Goode'

doc = """
Main Coordination Game
"""


class Constants(BaseConstants):
    name_in_url = 'main'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
    def before_session_starts(self):
        # Set up network (every group in subsession)
        for group in self.get_groups():
            network = Network(n_nodes = len(group.get_players()), 
                        description = self.session.config['network_description'],
                        nType = self.session.config['nType'])
            network.save()
            
            threshold_list = self.session.config['thresholds']
            threshold_list = [x.strip() for x in threshold_list.split(',')]            
            
            threshold_value = [randint(0,len(threshold_list) - 1) for i in range(network.n_nodes)]   
            
            network.addNodes(group, threshold_value, threshold_list)
            network.addEdges()
            
            self.network = network


        # Set up network from var parameters:
        for p in self.get_players():
            wall = Wall.objects.create(owner = p)
            wall.message_set.add(
                Message(createdBy=p, 
                        message='Hi, Player {}!'.format(p.id_in_group)
                )
            )
    
    network = models.ForeignKey(Network, default = 1)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    def get_messages(self):
        wall = self.wall_set.first()
        wall_messages = wall.message_set.all()

        wall_out = [m.to_dict() for m in wall_messages]

        return wall_out

    def get_neighbors(self):
        results = Edge.objects.filter(node_from = self.node)
        neighbors = [r.node_to for r in results]
        return neighbors

    def get_avatar(self):
        return self.participant.vars['avatar-src']
        
    def get_user_name(self):
        return self.participant.vars['user-name']

    node = models.ForeignKey(Node, default = 1)
    participate = models.BooleanField()

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
