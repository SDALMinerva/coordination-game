from channels import Group
from channels.sessions import channel_session
from .models import Player, Wall, Message, PrivateMessage, PrivateMessageBoard
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
        player_wall = Player.objects.get(id = data['wallId'])
        createdBy = Player.objects.get(id = data['createdBy'])
        messageRound = data['messageRound']
        message = Message(createdBy=createdBy, message=data['text'], messageRound=messageRound)
        player_wall.wall_set.first().message_set.add(message)

        if player_wall.session.config['instant_messaging'] == 'True':
            toSend = {
                'type': ws_data['type'],
                'content': message.to_dict(),
            }
            Group('chat-' + label).send({'text': json.dumps(toSend)})

    elif ws_data['type'] == 'private':
        
        data = ws_data['content']
        createdBy = Player.objects.get(id = data['createdBy'])
        messageRound = data['messageRound']

        if data['recipientId'] != "all":        
            player = Player.objects.get(id = data['recipientId'])
            private_message = PrivateMessage(createdBy=createdBy, message=data['text'], messageRound=messageRound)
            player.privatemessageboard_set.first().privatemessage_set.add(private_message)

            if player.session.config['instant_messaging'] == 'True':
                toSend = {
                    'type': ws_data['type'],
                    'content': private_message.to_dict(),
                }
                Group('chat-private-' + str(player.id)).send({'text': json.dumps(toSend)})
                
        else:
            for player in createdBy.get_neighbors():
                private_message = PrivateMessage(createdBy=createdBy, message=data['text'], messageRound=messageRound)
                player.privatemessageboard_set.first().privatemessage_set.add(private_message)

                if player.session.config['instant_messaging'] == 'True':
                    toSend = {
                        'type': ws_data['type'],
                        'content': private_message.to_dict(),
                    }
                    Group('chat-private-' + str(player.id)).send({'text': json.dumps(toSend)})

    elif ws_data['type'] == 'list':
        data = ws_data['content']
        player_wall = Player.objects.get(id = data['playerId'])      
        
        if player_wall.session.config['instant_messaging'] == 'True':
            entryList = player_wall.wall_set.first().message_set.all().order_by('datetime')
        else:
            P = player_wall.group.get_player_by_id(1)
            messageRound = P.participant.vars['message_round']
            entryList = player_wall.wall_set.first().message_set.filter(messageRound__lt = messageRound).order_by('datetime')
        entries = [entry.to_dict() for entry in entryList]
        toSend = {
            'type': ws_data['type'],
            'content': entries,
            }
        Group('chat-' + label).send({'text': json.dumps(toSend)})

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)
