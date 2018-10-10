from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Message, PrivateMessage
from random import random, randint
import json
from django.db.models import Count


class AssignAvatar(Page):
    template_name = 'practice/AssignAvatar.html'
    
    def is_displayed(self):
        return self.participant.vars['practice-continue'] and self.participant.vars['consent']
        
    pass

class Discuss(Page):

    template_name = 'practice/Discuss.html'

    def is_displayed(self):
        return self.participant.vars['practice-continue'] and (self.subsession.session.config['condition_messaging'] != 'none') and self.participant.vars['consent']

    def vars_for_template(self):
        group_players = self.group.get_players()
        message_round = group_players[0].participant.vars['message_round']
        
        if self.session.config['instant_messaging'] == 'True':
            message_round = -1
            
        if self.session.config['condition_network_knowledge'] == 'global':
            nodes = self.group.network.getNodes()
            edges = self.group.network.getEdges()
            networkDisplay = 'The'
        elif self.session.config['condition_network_knowledge'] == 'local':
            nodes = self.group.network.get_nodes_from_player(self.player)
            edges = self.group.network.get_edges_from_player(self.player)
            networkDisplay = 'Your'
        else:
            nodes = []
            edges = []

        for node in nodes:
            string = node['label'].split('\n')
            if string[0] == self.player.get_user_name():
                string[0] += ' (You)'
            node['label'] = '\n'.join(string)        
            
        if self.session.config['show_network_threshold'] == 'False':
            for node in nodes:
                node['label'] = node['label'].split('\n')[0]
            
        group_dict = dict([(node.avatar.get_name(), node.avatar.src) for node in self.group.network.node_set.all()])
        group_dict[self.player.get_user_name() + ' (you)'] = group_dict[self.player.get_user_name()]
        del group_dict[self.player.get_user_name()]
        
        player_node = self.player.node     
        posted_wall_messages = Message.objects.filter(messageRound = message_round)
        posted_wall_messages = posted_wall_messages.exclude(deleted = True)
        posted_wall_messages = posted_wall_messages.filter(createdBy = player_node)

        wall_counts = posted_wall_messages.values('wall__node').annotate(count=Count('wall__node'))
        wall_counts = {r['wall__node']:r['count'] for r in wall_counts}

        posted_pm_messages = PrivateMessage.objects.filter(messageRound = message_round)
        posted_pm_messages = posted_pm_messages.exclude(deleted = True)
        posted_pm_messages = posted_pm_messages.filter(createdBy = player_node)
        
        pm_counts = posted_pm_messages.values('wall__node').annotate(count=Count('wall__node'))
        pm_counts = {r['wall__node']:r['count'] for r in pm_counts}    
        
        comm_type = self.session.config['condition_messaging']
        network_type = self.session.config['condition_network_knowledge']
        screenImage = 'instructions/screenshot-{}-{}.png'     

        initEntryTable = 'none'
        if comm_type == 'bilateral':
            initEntryTable = self.player.get_private_entry_table()
        if comm_type == 'wall':
            initEntryTable = self.player.get_entry_table()        
        
        return {
        'avatar': self.player.get_avatar(),
        'user_name': self.player.get_user_name(),
        'avatars': dict([(node.id, node.avatar.src) for node in self.group.network.node_set.all()]),
        'thresholds': dict([(node.id, node.threshold_text) for node in self.group.network.node_set.all()]),
        'user_names': dict([(node.id, node.avatar.get_name()) for node in self.group.network.node_set.all()]),
        'neighbor_net': dict(zip([node.id for node in self.player.get_neighbors()],[[node.id for node in P.get_neighbors()] for P in self.player.get_neighbors()])),
        'neighbors': [node.id for node in self.player.get_neighbors()],    
        'messages': Constants.messages,
        'wall': json.dumps(self.player.get_messages()),
        'privateMessages': json.dumps(self.player.get_private_messages()), 
        'nodes': json.dumps(nodes),
        'edges': json.dumps(edges),
        'messageRound': message_round,
        'lastRound': message_round == Constants.num_messaging_rounds,
        'networkDisplay': networkDisplay,
        'group': group_dict,
        'wall_sent_to': wall_counts,
        'pm_sent_to': pm_counts,
        'screenImage': screenImage.format(comm_type,network_type),
        'initEntryTable': json.dumps(initEntryTable),
        }

class BeginWaitPage(WaitPage):

    template_name = 'main/wait_page.html'

    def is_displayed(self):
        return self.participant.vars['practice-continue'] and self.participant.vars['consent']

    def after_all_players_arrive(self):
        pass
        

class IntermediateWaitPage(WaitPage):

    template_name = 'main/wait_page.html'

    def is_displayed(self):
        return self.participant.vars['practice-continue'] and self.participant.vars['consent']

    def after_all_players_arrive(self):
        group_players = self.group.get_players()

### SIMPLE CODE FOR AUTOMATED MESSAGES
        message_round = group_players[0].participant.vars['message_round']        
        for node in self.group.network.node_set.all():
            if node.bot:
                neighbors = node.get_neighbors()
                for neighbor in neighbors:
                    if int(round(random())) and (self.session.config['condition_messaging'] in ['wall','both']):
                        wall = neighbor.wall_set.first()
                        wall.message_set.add(
                            Message(createdBy=node,
                            messageRound = message_round, 
                            message=Constants.messages[randint(1,2)]
                            )
                        )
                    
                    if int(round(random())) and (self.session.config['condition_messaging'] in ['bilateral','both']):    
                        privateMessageBoard = neighbor.privatemessageboard_set.first()
                        privateMessageBoard.privatemessage_set.add(
                        PrivateMessage(createdBy=node,
                            messageRound = message_round, 
                            message=Constants.messages[randint(1,2)]
                            )
                        )        
        
        group_players[0].participant.vars['message_round'] += 1


class EndWaitPage(WaitPage):

    template_name = 'main/wait_page.html'

    def is_displayed(self):
        return self.participant.vars['practice-continue'] and self.participant.vars['consent']

    def after_all_players_arrive(self):

        for node in self.group.network.node_set.all():
            if node.bot:
                node.participate = randint(0,1)
            else:
                node.participate = node.player_set.first().participate        
        
#        self.group.set_payoffs() #Not needed in practice round.
        group_players = self.group.get_players()
        group_players[0].participant.vars['message_round'] = 1        
        
        pass

class Decide(Discuss):
    
    template_name = 'practice/Decide.html'

    def is_displayed(self):
        return self.participant.vars['practice-continue'] and self.participant.vars['consent']   
    
    form_model = models.Player
    form_fields = [
        'participate'
    ]


class Continue(Page):

    def is_displayed(self):
        if self.player.subsession.round_number == Constants.num_rounds:
            self.template_name = 'practice/PracticeEnd.html'
        else:
            self.template_name = 'practice/Continue.html'
        return self.participant.vars['practice-continue'] and self.participant.vars['consent']

    def before_next_page(self):
        self.participant.vars['practice-continue'] = self.player.continue_practice
        
    form_model = models.Player
    form_fields = [
        'continue_practice'
    ]
      

class Intro(Page):
    template_name = 'practice/intro.html'
    
    def is_displayed(self):
        return (self.subsession.round_number == 1) and self.participant.vars['consent']

messaging_apps = [x for i in range(Constants.num_messaging_rounds) for x in [Discuss, IntermediateWaitPage]]
seq = [Intro, AssignAvatar, BeginWaitPage]
seq.extend(messaging_apps)
seq.extend([Decide, EndWaitPage, Continue])

page_sequence = seq
