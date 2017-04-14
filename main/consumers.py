from channels import Group
from channels.sessions import channel_session
from .models import Player, Wall, Message
import json

@channel_session
def ws_connect(message):
    label = message['path'].split('/')[-1]
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = label

@channel_session
def ws_receive(message):
    label = message.channel_session['room']
    ws_data = json.loads(message['text'])
    if ws_data['type'] == 'send':
        data = ws_data['content']
        player_wall = Player.objects.get(id = data['wallId'])
        createdBy = Player.objects.get(id = data['createdBy'])
        message = Message(createdBy=createdBy, message=data['text'])
        player_wall.wall_set.first().message_set.add(message)

        toSend = {
            'type': ws_data['type'],
            'content': message.to_dict(),
        }

        Group('chat-' + label).send({'text': json.dumps(toSend)})

    elif ws_data['type'] == 'list':
        data = ws_data['content']
        player_wall = Player.objects.get(id = data['playerId'])
        entryList = player_wall.wall_set.first().message_set.all().order_by('datetime');
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
