from channels import Group
from channels.sessions import channel_session
from .models import Player, Wall, Message, PrivateMessage, PrivateMessageBoard
from network.models import Node
import json

@channel_session
def ws_connect(message):
    label = message['path'].split('/')[-1]
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = label  
    message.reply_channel.send({'accept': True})

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    ws_data = json.loads(message['text'])
    if ws_data['type'] == 'send':
        data = ws_data['content']
        node = Node.objects.get(id = data['wallId'])
        createdBy = Node.objects.get(id = data['createdBy'])
        messageRound = data['messageRound']
        message = Message(createdBy=createdBy, message=data['text'], messageRound=messageRound, key=data['key'])
        wall = node.wall_set.first()
        wall.message_set.add(message)

        participant = createdBy.player_set.first().participant
        participant.vars['discuss_participate'] = True
        participant.save()

        if wall.subsession.session.config['instant_messaging'] == 'True':
            toSend = {
                'type': ws_data['type'],
                'content': message.to_dict(),
            }
            Group('chat-' + label).send({'text': json.dumps(toSend)})
    
    elif ws_data['type'] == 'wall-delete':
        data = ws_data['content']
        node = Node.objects.get(id = data['wallId'])
        wall = node.wall_set.first()
        message = wall.message_set.get(key=data['key'])
        message.deleted = True

        message.save()
        
    elif ws_data['type'] == 'private-delete':
        data = ws_data['content']
        node = Node.objects.get(id = data['wallId'])
        wall = node.privatemessageboard_set.first()
        message = wall.privatemessage_set.get(key=data['key'])
        message.deleted = True

        message.save()

    elif ws_data['type'] == 'private':
        
        data = ws_data['content']
        createdBy = Node.objects.get(id = data['createdBy'])
        messageRound = data['messageRound']

        participant = createdBy.player_set.first().participant
        participant.vars['discuss_participate'] = True
        participant.save()

        if data['recipientId'] != "all":        
            node = Node.objects.get(id = data['recipientId'])
            private_message = PrivateMessage(createdBy=createdBy, message=data['text'], messageRound=messageRound, key=data['key'])
            message_board = node.privatemessageboard_set.first()
            message_board.privatemessage_set.add(private_message)

            if message_board.subsession.session.config['instant_messaging'] == 'True':
                toSend = {
                    'type': ws_data['type'],
                    'content': private_message.to_dict(),
                }
                Group('chat-private-' + str(node.id)).send({'text': json.dumps(toSend)})
               
        else:
            for node in createdBy.get_neighbors():
                private_message = PrivateMessage(createdBy=createdBy, message=data['text'], messageRound=messageRound, key=data['key'])
                message_board = player.privatemessageboard_set.first()
                message_board.privatemessage_set.add(private_message)

                if message_board.subsession.session.config['instant_messaging'] == 'True':
                    toSend = {
                        'type': ws_data['type'],
                        'content': private_message.to_dict(),
                    }
                    Group('chat-private-' + str(node.id)).send({'text': json.dumps(toSend)})

    elif ws_data['type'] == 'list':
        data = ws_data['content']
        node = Node.objects.get(id = data['playerId'])
        player_node = Node.objects.get(id = data['sentBy'])      
        
        wall = node.wall_set.first()
        if wall.subsession.session.config['instant_messaging'] == 'True':
            entryList = wall.message_set.all().order_by('datetime')
        else:
            # Note: will not work for all-automated code (e.g., has to be at least 1 player in the group)
            P = node.network.group_set.first().get_player_by_id(1)
            messageRound = P.participant.vars['message_round']
#            entryList = node.wall_set.first().message_set.filter(messageRound__lt = messageRound).order_by('datetime')
            
            past_wall_messages = wall.message_set.filter(messageRound__lt = messageRound)
            past_wall_messages = past_wall_messages.exclude(deleted = True)
            posted_wall_messages = wall.message_set.filter(createdBy = player_node)
            posted_wall_messages = posted_wall_messages.exclude(deleted = True)
            
            entryList = past_wall_messages | posted_wall_messages
            entryList.order_by('datetime')
                       
        entries = [entry.to_dict() for entry in entryList]
        toSend = {
            'type': ws_data['type'],
            'content': entries,
            }
        Group('chat-' + label).send({'text': json.dumps(toSend)})#
    
        
    elif ws_data['type'] == 'private-list':
        data = ws_data['content']
        node = Node.objects.get(id = data['playerId'])
        player_node = Node.objects.get(id = data['sentBy'])      
        
        wall = node.privatemessageboard_set.first()
        if wall.subsession.session.config['instant_messaging'] == 'True':
            entryList = wall.message_set.all().order_by('datetime')
        else:
            # Note: will not work for all-automated code (e.g., has to be at least 1 player in the group)
            P = node.network.group_set.first().get_player_by_id(1)
            messageRound = P.participant.vars['message_round']
#            entryList = node.wall_set.first().message_set.filter(messageRound__lt = messageRound).order_by('datetime')
            
            #DOMINGO- Left off here... (should be last fix)
            past_wall_messages = wall.privatemessage_set.filter(messageRound__lt = messageRound)
            past_wall_messages = past_wall_messages.exclude(deleted = True)
            posted_wall_messages_to = PrivateMessage.objects.filter(createdBy = player_node, wall__node = node)
            posted_wall_messages_to = posted_wall_messages_to.exclude(deleted = True)
            posted_wall_messages_from = PrivateMessage.objects.filter(createdBy = node, wall__node = player_node)
            posted_wall_messages_from = posted_wall_messages_to.exclude(deleted = True)
            
            entryList = past_wall_messages | posted_wall_messages_to | posted_wall_messages_from
            entryList.order_by('datetime')
                
        entries = [entry.to_dict() for entry in entryList]
        toSend = {
            'type': 'list',
            'content': entries,
            }
        Group('chat-' + label).send({'text': json.dumps(toSend)})#
    
    
    elif ws_data['type'] == 'entry-table':
        data = ws_data['content']
        player_node = Node.objects.get(id = data['sentBy'])      
        
        # Note: will not work for all-automated code (e.g., has to be at least 1 player in the group)
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
            
        toSend = {
            'type': ws_data['type'],
            'content': list(table.values()),
            }
        Group('chat-' + label).send({'text': json.dumps(toSend)})#
        
        
    elif ws_data['type'] == 'private-entry-table':
        print('Private!!!')
        data = ws_data['content']
        player_node = Node.objects.get(id = data['sentBy'])      
        
        # Note: will not work for all-automated code (e.g., has to be at least 1 player in the group)
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
            
        toSend = {
            'type': 'entry-table',
            'content': list(table.values()),
            }
        Group('chat-' + label).send({'text': json.dumps(toSend)})#
        
        
    elif ws_data['type'] == 'participate_flag':
        data = ws_data['content']
        player_node = Node.objects.get(id = data['createdBy'])
        participant = player_node.player_set.first().participant
        participant.vars['discuss_participate'] = True
        participant.save()
        
    elif ws_data['type'] == 'moved_on_flag':
        data = ws_data['content']
        player_node = Node.objects.get(id = data['createdBy'])
        node_group = player_node.network.getNodes()
        toSend = {
                'type': 'moved_on',
                'content': player_node.avatar.get_name(),
            }
        for node in node_group:
            Group('chat-comm-' + str(node['id'])).send({'text': json.dumps(toSend)})
        

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)
