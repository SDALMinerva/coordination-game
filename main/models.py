from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from avatar.models import Avatar

from network.models import Network, Edge, Node
from random import randint
import json

author = 'Brian J. Goode'

doc = """
Main Coordination Game
"""


# Open Round Specification
with open('./main/round_specs/seq-48rounds.json') as oFile:
    round_specs = json.load(oFile)


class Constants(BaseConstants):
    name_in_url = 'coordinate'
    players_per_group = 5
    num_rounds = 2
    num_messaging_rounds = 2


class Subsession(BaseSubsession):
	
    def creating_session(self):
        
        # Threshold Options from Session Config
        threshold_list = self.session.config['thresholds']
        threshold_list = [x.strip() for x in threshold_list.split(',')]


        # Player Assignment from Round Specification
        player_assignments = round_specs[str(self.round_number)]['positions']
        group_matrix = [player_assignments[i*5:i*5+5] for i in range(3)]
        self.set_group_matrix(group_matrix)


        # Avatar Assignments from Round Specification
        avatar_assignments = iter(round_specs[str(self.round_number)]['avatars'])
        for p in self.get_players():
            p.avatar = Avatar.objects.get(src = next(avatar_assignments))
            p.user_name = p.avatar.name.split('-')[0]
            

        # Set up network (every group in subsession)
        network_spec = round_specs[str(self.round_number)]['network']
        network_type, network_threshold = network_spec.split('-')
        network_threshold = [int(x) for x in network_threshold if x.isdigit()]
        for group in self.get_groups():
            network = Network(n_nodes = len(group.get_players()), 
                        description = network_spec,
                        nType = 'star')
            network.save()            
            
            network.addNodes(group, network_threshold, threshold_list)
            network.addEdges()
            
            group.network = network


        # Initiate Wall:
        for p in self.get_players():
            if p.id_in_group == 1:
                p.participant.vars['message_round'] = 1
                
            wall = Wall.objects.create(owner = p)
#            wall.message_set.add(
#                Message(createdBy=p,
#                        messageRound = 0, 
#                        message='Hi, Player {}!'.format(p.id_in_group)
#                )
#            )

        # Thresholds for Players (stylistic):
        for p in self.get_players():
            p.threshold = int(p.node.threshold_text)

class Group(BaseGroup):
    network = models.ForeignKey(Network, default = 1)
    
    def set_payoffs(self):
        for p in self.get_players():
            if p.participate:
                group = p.get_others_in_group()
            
                n_participants = 1
                for player in group:
                    if player.participate:
                        n_participants += 1
                    
                if p.threshold < n_participants:
                    p.payoff = self.session.config['payoff_above_threshold']
                else:
                    p.payoff = self.session.config['payoff_below_threshold']
                
            else:
                p.payoff = self.session.config['payoff_no_participate']       
            
    pass


class Player(BasePlayer):
    
    def get_messages(self):
        wall = self.wall_set.first()
        
        if self.session.config['instant_messaging'] == 'True':
            wall_messages = wall.message_set.all()
        else:
            p = self.group.get_player_by_id(1)
            messageRound = p.participant.vars['message_round']
            wall_messages = wall.message_set.filter(messageRound__lt = messageRound)

        wall_out = [m.to_dict() for m in wall_messages]
        return wall_out

    def get_neighbors(self):
        results = Edge.objects.filter(node_from = self.node)
        neighbors = [Player.objects.get(node=r.node_to) for r in results]
        return neighbors

    def get_avatar(self):
        return self.avatar.src
        
    def get_user_name(self):
        return self.user_name

    node = models.ForeignKey(Node, default = 1)
    threshold = models.IntegerField()
    participate = models.BooleanField()
    
    # Avatar Portions
    user_name = models.CharField(default = 'Not Assigned')
    avatar = models.ForeignKey(Avatar, default = 1, related_name = 'avatar_seq')


class Wall(models.Model):
    owner = models.ForeignKey(Player)


class Message(models.Model):
    wall = models.ForeignKey(Wall)
    createdBy = models.ForeignKey(Player)
    datetime = models.DateTimeField(auto_now=True)
    message = models.CharField()
    messageRound = models.IntegerField()

    def to_dict(self):
        return {
            'timestamp': self.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'content': self.message,
            'author': 'Player {}'.format(self.createdBy_id)
            } 


class PrivateMessageBoard(models.Model):
    owner = models.ForeignKey(Player)
    
    
class PrivateMessage(models.Model):
    wall = models.ForeignKey(PrivateMessageBoard)
    createdBy = models.ForeignKey(Player)
    datetime = models.DateTimeField(auto_now=True)
    message = models.CharField()
    messageRound = models.IntegerField()

    def to_dict(self):
        return {
            'timestamp': self.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'content': self.message,
            'author': 'Player {}'.format(self.createdBy_id)
            } 