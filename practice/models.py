from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from avatar.models import Avatar

from practice_network.models import Network, Edge, Node
from random import randint
import json

author = 'Brian J. Goode, Ethan Vu'

doc = """
Main Coordination Game - Practice
"""


# Open Round Specification
with open('./practice/round_specs/seq-48rounds-practice.json') as oFile:
    round_specs = json.load(oFile)


class Constants(BaseConstants):
    name_in_url = 'practice'
    chat_name = 'practice-chat'
    players_per_group = None               #EDIT: Make flexible with number of players.
    num_rounds = 3                     #EDIT: Make adjustable from session config.
    num_messaging_rounds = 1            #EDIT: Make adjustable from session config.
    messages = {
            1: 'I will participate.',
            2: 'I will not participate.',
            }


class Subsession(BaseSubsession):
	
    def creating_session(self):
        
        # Threshold Options from Session Config
        threshold_list = self.session.config['thresholds']
        threshold_list = [x.strip() for x in threshold_list.split(',')]

        #################################################
        #### BEGIN GROUP ASSIGNMENT / BOT ADJUSTMENT ####
        #################################################
        
        # To-do: Handle Dropouts mid-game.
        
        # Player Assignment from Round Specification
        n_players = self.session.num_participants
        player_assignments = round_specs[str(self.round_number)]['positions']
        group_matrix_full = [player_assignments[i*5:i*5+5] for i in range(3)]  #hard-coded group size and #!
        group_matrix = [[p for p in player_assignments[i*5:i*5+5] if p <= n_players] for i in range(3)] #hard-coded group size and number!

        # For Practice Round, Give Each Player They're Own Group:
            
        ## SEPARATE IDENTITIES:
        group_matrix_full = [group_matrix_full[i] for i in range(len(group_matrix)) for j in range(len(group_matrix[i]))]
        group_matrix = [[entry] for row in group_matrix for entry in row]

        self.set_group_matrix(group_matrix)


        # Avatar Assignments from Round Specification (not affected by # players; i.e. goes in order of player...)
        avatar_assignments = iter(round_specs[str(self.round_number)]['avatars'])
        for p in self.get_players():
            p.avatar = Avatar.objects.get(src = next(avatar_assignments))
            p.user_name = p.avatar.name.split('-')[0]
            p.participant.vars['practice-continue'] = True
            

        # Set up network (every group in subsession)
        # Only create network for active players.
        network_spec = round_specs[str(self.round_number)]['network']
        network_type, network_threshold = network_spec.split('-')
        network_threshold = [int(x) for x in network_threshold if x.isdigit()]
        
        group_id = 0
        for group, eligible_players in zip(group_matrix_full, group_matrix):
            network = Network(n_nodes = len(group), 
                        description = network_spec,
                        nType = network_type)                     
            network.save()            

            players = []
            for subsession_id in group:
                if subsession_id in eligible_players:
                    players.append(self.get_players()[subsession_id-1])
                else:
                    players.append(False)          
            
            avatars = [round_specs[str(self.round_number)]['avatars'][i-1] for i in group]
            network.addNodes(players, network_threshold, threshold_list, avatars)
            network.addEdges()
            
            G = self.get_groups()
            if G[group_id]:
                G[group_id].network = network
            group_id += 1
        
        # To-do: Tie Wall behavior to Network Spec rather than number of players.
        # Initiate Wall:
        for p in self.get_players():
            if p.id_in_group == 1:
                p.participant.vars['message_round'] = 1
        
        for group in self.get_groups():
            for node in group.network.node_set.all():       
                wall = Wall.objects.create(node=node,subsession=self)
                privateMessageBoard = PrivateMessageBoard.objects.create(node=node,subsession=self)

        # Thresholds for Players (stylistic):
        for p in self.get_players():
            p.threshold = int(p.node.threshold_text)
                        
        ###############################################    
        #### END GROUP ASSIGNMENT / BOT ADJUSTMENT ####
        ###############################################
        

class Group(BaseGroup):
    network = models.ForeignKey(Network, default = 1)
    
    def set_payoffs(self):
        for p in self.get_players():
            if p.participate:
                group_nodes = p.node.network.node_set.all()
            
                n_participants = 0
                for node in group_nodes:
                    if node.participate:
                        n_participants += 1
                    
                if p.threshold < n_participants:
                    p.round_payoff = self.session.config['payoff_above_threshold']
                else:
                    p.round_payoff = self.session.config['payoff_below_threshold']
                
            else:
                p.round_payoff = self.session.config['payoff_no_participate']
                
            if self.subsession.round_number == int(self.session.config['payoff_round']):
                p.payoff = p.round_payoff       
            
    pass


class Player(BasePlayer):
      
    def get_entry_table(self):
        player_node = self.node
        P = player_node.network.group_set.first().get_player_by_id(1)
        messageRound = P.participant.vars['message_round']

        posted_wall_messages = Message.objects.filter(messageRound = messageRound)
        posted_wall_messages = posted_wall_messages.exclude(deleted = True)
        posted_wall_messages = posted_wall_messages.filter(createdBy = player_node)

        entryList = posted_wall_messages

        message_list = player_node.wall_set.first().subsession.session.config['messages'].split('/')
        neighbor_list = list(set(player_node.get_neighbors()))
        
        table = {}
        for n in neighbor_list:
            table[n.avatar.get_name()] = {'name': n.avatar.get_name(), 'icon': n.avatar.src, '0': False, '1': False}
        
        table[player_node.avatar.get_name()] = {'name': player_node.avatar.get_name() + ' (you)', 'icon': player_node.avatar.src, '0': False, '1': False}

        for entry in entryList:
            name = entry.wall.node.avatar.get_name()
            table[name]['0'] = ((entry.message== message_list[0]) or table[name]['0'])
            table[name]['1'] = ((entry.message== message_list[1]) or table[name]['1'])    
    
        return list(table.values())
        

    def get_private_entry_table(self):
        player_node = self.node
        P = player_node.network.group_set.first().get_player_by_id(1)
        messageRound = P.participant.vars['message_round']

        posted_wall_messages = PrivateMessage.objects.filter(messageRound = messageRound)
        posted_wall_messages = posted_wall_messages.exclude(deleted = True)
        posted_wall_messages = posted_wall_messages.filter(createdBy = player_node)

        entryList = posted_wall_messages

        message_list = player_node.privatemessageboard_set.first().subsession.session.config['messages'].split('/')
        neighbor_list = set(player_node.get_neighbors())
        
        table = {}
        for n in neighbor_list:
            table[n.avatar.get_name()] = {'name': n.avatar.get_name(), 'icon': n.avatar.src, '0': False, '1': False}
        
        for entry in entryList:
            name = entry.wall.node.avatar.get_name()
            table[name]['0'] = ((entry.message== message_list[0]) or table[name]['0'])
            table[name]['1'] = ((entry.message== message_list[1]) or table[name]['1']) 
            
        return list(table.values())
        
        
    def get_messages(self):
        wall = self.node.wall_set.first()
        
        if self.session.config['instant_messaging'] == 'True':
            wall_messages = wall.message_set.all()
        else:
            p = self.group.get_player_by_id(1)
            messageRound = p.participant.vars['message_round']
            past_wall_messages = wall.message_set.filter(messageRound__lt = messageRound)
            past_wall_messages = past_wall_messages.exclude(deleted = True)
            posted_wall_messages = wall.message_set.filter(createdBy = self.node)
            posted_wall_messages = posted_wall_messages.exclude(deleted = True)
            
            wall_messages = past_wall_messages | posted_wall_messages

        wall_out = [m.to_dict() for m in wall_messages]
        return wall_out
        
    def get_private_messages(self):
        pmb = self.node.privatemessageboard_set.first()
        
        if self.session.config['instant_messaging'] == 'True':
            private_messages = pmb.privatemessage_set.all()
        else:
            p = self.group.get_player_by_id(1)
            messageRound = p.participant.vars['message_round']
            private_messages = pmb.privatemessage_set.filter(messageRound__lt = messageRound)

        pmb_out = [m.to_dict() for m in private_messages]
        return pmb_out

    def get_neighbors(self):
        results = Edge.objects.filter(node_from = self.node)
#        neighbors = [Player.objects.get(node=r.node_to) for r in results]
        neighbors = [r.node_to for r in results]
        return neighbors

    def get_avatar(self):
        return self.avatar.src
        
    def get_user_name(self):
        return self.user_name

    node = models.ForeignKey(Node, default = 1)
    threshold = models.IntegerField()
    participate = models.BooleanField(verbose_name="Will you participate?")
    
    # Avatar Portions
    user_name = models.CharField(default = 'Not Assigned')
    avatar = models.ForeignKey(Avatar, default = 1, related_name = 'practice_avatar_seq')
    
    # Round_Payoff
    round_payoff = models.CurrencyField();
    message_cost = models.CurrencyField();
    
    continue_practice = models.BooleanField(
        verbose_name="Would you like to continue with practice rounds?",
        blank = True,
        initial = True,
        choices = [
            [True, "Yes, I would like to continue practicing."],
            [False,"No, I understand the game and would like to advance to the main rounds."],        
        ]);


class Wall(models.Model):
    subsession = models.ForeignKey(Subsession)
    node = models.ForeignKey(Node)


class Message(models.Model):
    wall = models.ForeignKey(Wall)
    createdBy = models.ForeignKey(Node)
    datetime = models.DateTimeField(auto_now=True)
    message = models.CharField()
    messageRound = models.IntegerField()
    deleted = models.BooleanField(initial=False)
    key = models.CharField()

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'content': self.message,
            'author': 'Player {}'.format(self.createdBy_id),
            'messageRound': self.messageRound,
            'key': self.key,
            } 


class PrivateMessageBoard(models.Model):
    subsession = models.ForeignKey(Subsession)
    node = models.ForeignKey(Node)
    
    
class PrivateMessage(models.Model):
    wall = models.ForeignKey(PrivateMessageBoard)
    createdBy = models.ForeignKey(Node)
    datetime = models.DateTimeField(auto_now=True)
    message = models.CharField()
    messageRound = models.IntegerField()
    deleted = models.BooleanField(initial=False)
    key = models.CharField()

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            'content': self.message,
            'author': 'Player {}'.format(self.createdBy_id),
            'messageRound': self.messageRound,
            'key': self.key,
            } 
            
            
            
