from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json


class AssignAvatar(Page):
   
    pass

class Discuss(Page):

    def vars_for_template(self):
        group_players = self.group.get_players()
        message_round = group_players[0].participant.vars['message_round']
        
        if self.session.config['instant_messaging'] == 'True':
            message_round = -1
            
        if self.session.config['condition_network_knowledge'] == 'global':
            nodes = self.group.network.getNodes()
            edges = self.group.network.getEdges()
            networkDisplay = 'Group'
        elif self.session.config['condition_network_knowledge'] == 'local':
            nodes = self.group.network.get_nodes_from_player(self.player)
            edges = self.group.network.get_edges_from_player(self.player)
            networkDisplay = 'Your'
        else:
            nodes = []
            edges = []
            
        
        return {
        'avatar': self.player.get_avatar(),
        'user_name': self.player.get_user_name(),
        'avatars': dict([(p.id, p.get_avatar()) for p in group_players]),
        'thresholds': dict([(p.id, p.node.threshold_text) for p in group_players]),
        'user_names': dict([(p.id, p.get_user_name()) for p in group_players]),
        'neighbor_net': dict(zip([p.id for p in self.player.get_neighbors()],[[p.id for p in P.get_neighbors()] for P in self.player.get_neighbors()])),
        'neighbors': [p.id for p in self.player.get_neighbors()],    
        'messages': {
            1: 'I will participate.',
            2: 'I will not participate.',
            },
        'wall': json.dumps(self.player.get_messages()),
        'privateMessages': json.dumps(self.player.get_private_messages()), 
        'nodes': json.dumps(nodes),
        'edges': json.dumps(edges),
        'messageRound': message_round,
        'lastRound': message_round == Constants.num_messaging_rounds,
        'networkDisplay': networkDisplay,
        }

class BeginWaitPage(WaitPage):

    template_name = 'main/wait_page.html'

    def after_all_players_arrive(self):
        pass
        

class IntermediateWaitPage(WaitPage):

    template_name = 'main/wait_page.html'

    def after_all_players_arrive(self):
        group_players = self.group.get_players()
        group_players[0].participant.vars['message_round'] += 1


class EndWaitPage(WaitPage):

    template_name = 'main/wait_page.html'

    def after_all_players_arrive(self):
        
        self.group.set_payoffs()        
        
        pass

class Decide(Page):
    form_model = models.Player
    form_fields = [
        'participate'
    ]
    pass

messaging_apps = [x for i in range(Constants.num_messaging_rounds) for x in [Discuss, IntermediateWaitPage]]
seq = [AssignAvatar, BeginWaitPage]
seq.extend(messaging_apps)
seq.extend([Decide, EndWaitPage])

page_sequence = seq
