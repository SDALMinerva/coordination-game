from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from random import shuffle
from itertools import combinations, product

author = 'Brian J. Goode'

doc = """
Manages the network interactions in the game.
"""


class Constants(BaseConstants):
    name_in_url = 'network'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Network(models.Model):
    n_nodes = models.IntegerField(default = -1)
    description = models.CharField()
    nType = models.CharField()

    def __str__(self):
        return 'Id: {}\n{}'.format(self.id, self.description)

    def getNodes(self):
        nodes = [{
            'id': node.id,
            'shape': 'circularImage',
            'image': '/static/avatar/{}'.format(node.player_set.first().get_avatar()),
            'label': '{}\nThreshold: {}'.format(node.player_set.first().get_user_name(), node.threshold_text),
        } for node in self.node_set.all()]
        return nodes


    def getEdges(self, directed = False):
        pairs = self.edge_set.all().values_list('node_to', 'node_from')
        
        if not directed:
            pairs = list(set([tuple(sorted(pair)) for pair in pairs]))

        edges = [{'to': t, 'from': f,} for t,f in pairs]
        return edges
        
    
    def get_nodes_from_player(self, player):
        
        edge_list = self.edge_set.filter(node_from__player = player)
        nodes = [{
            'id': edge.node_to.id,
            'shape': 'circularImage',
            'image': '/static/avatar/{}'.format(edge.node_to.player_set.first().get_avatar()),
            'label': '{}\nThreshold: {}'.format(edge.node_to.player_set.first().get_user_name(), edge.node_to.threshold_text),
        } for edge in edge_list]
        
        nodes.append({
            'id': player.node.id,
            'shape': 'circularImage',
            'image': '/static/avatar/{}'.format(player.get_avatar()),
            'label': '{}\nThreshold: {}'.format(player.get_user_name(), player.node.threshold_text),
        })

        return nodes
        
        
    def get_edges_from_player(self, player, directed = False):
        pairs = self.edge_set.filter(node_from__player = player).values_list('node_to', 'node_from')
        
        if not directed:
            pairs = list(set([tuple(sorted(pair)) for pair in pairs]))

        edges = [{'to': t, 'from': f,} for t,f in pairs]
        return edges
        

    def addNodes(self, group, threshold, threshold_text, shuffle = False):
        
        posis = list(range(1,self.n_nodes + 1))        
        
        if shuffle:
            shuffle(posis)
            
        for p, pos, thrs in zip(group.get_players(), posis, threshold):
            node = Node(
                    position = pos, 
                    network=self, 
                    threshold=thrs,
                    threshold_text=threshold_text[thrs],
                    )
            node.save()
            p.node = node
        return 


    def addEdges(self, directed = False):
        
        n = self.n_nodes
        nType = self.nType

        if nType == 'clique':
            edges = combinations(range(1,n+1), 2)

        elif nType == 'star':
            edges = product([1], range(2,n+1))

        elif nType == 'circle':
            edges = zip(range(1,n+1),[i - (i // (n+1))*n for i in range(2,n+2)])

        else:
            edges = []

        for n1, n2 in edges:
            node1 = Node.objects.get(network=self, position=n1)
            node2 = Node.objects.get(network=self, position=n2)
            edge = Edge(network = self, node_from = node1, node_to = node2)
            edge.save()
            
            if not directed:
                edge = Edge(network = self, node_from = node2, node_to = node1)
                edge.save()

        return


class Node(models.Model):
    position = models.IntegerField()
    network = models.ForeignKey(Network)
    threshold = models.FloatField(default = -1)
    threshold_text = models.CharField()
    
    def __str__(self):
        return 'P: {} - T: {}'.format(self.position, self.threshold)


class Edge(models.Model):
    network = models.ForeignKey(Network)
    node_from = models.ForeignKey(Node, related_name="node_from")
    node_to = models.ForeignKey(Node, related_name="node_to")

        
