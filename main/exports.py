import csv
import datetime

from django.http import HttpResponse

import vanilla

from .models import Message, PrivateMessage, Network


class WallMessageExport(vanilla.View):

    url_name = 'main_wallmessage_export'
    url_pattern = '^main_wallmessage_export/$'
    display_name = 'Wall Messages export'

    def get(request, *args, **kwargs):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            'Wall Messages (accessed {}).csv'.format(
                datetime.date.today().isoformat()
            )
        )

        messages = Message.objects.order_by('datetime')
        rows = []
        
        for m in messages:
            createdBy_code = 'BOT'
            if m.createdBy.player_set.first():
                createdBy_code = m.createdBy.player_set.first().participant.code
            wall_code = 'BOT'
            if m.wall.node.player_set.first():
                wall_code = m.wall.node.player_set.first().participant.code
            row = (
                m.wall.subsession.session.code,
                m.wall.subsession.round_number,
                m.wall.node.network_id,
                m.wall.node.network.group_set.first().id_in_subsession,
                m.wall.node.network.nType,
                m.createdBy.bot,
                createdBy_code,
                m.createdBy.avatar.get_name(),
                m.createdBy.threshold,
                m.createdBy.position,
                m.wall.node.bot,
                wall_code,
                m.wall.node.avatar.get_name(),
                m.wall.node.threshold,
                m.wall.node.position,
                m.message,
                m.deleted,
                m.datetime,
            )
            rows.append(row)



        column_names = [
            'session.code',
            'subsession__round_number',
            'network_id',
            'network_position',
            'network_type',
            'createdBy__bot',
            'createdBy__code',
            'createdBy__avatar',
            'createdBy__threshold',
            'createdBy__position',
            'wall__node__bot',
            'wall__code',
            'wall__avatar',
            'wall__threshold',
            'wall__position',
            'message',
            'deleted',
            'datetime',
        ]

        writer = csv.writer(response)
        writer.writerows([column_names])
        writer.writerows(rows)

        return response
        
class PrivateMessageExport(vanilla.View):

    url_name = 'main_privatemessage_export'
    url_pattern = '^main_privatemessage_export/$'
    display_name = 'Private Messages export'

    def get(request, *args, **kwargs):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            'Private Messages (accessed {}).csv'.format(
                datetime.date.today().isoformat()
            )
        )

        messages = PrivateMessage.objects.order_by('datetime')
        rows = []
        
        for m in messages:
            createdBy_code = 'BOT'
            if m.createdBy.player_set.first():
                createdBy_code = m.createdBy.player_set.first().participant.code
            wall_code = 'BOT'
            if m.wall.node.player_set.first():
                wall_code = m.wall.node.player_set.first().participant.code
            row = (
                m.wall.subsession.session.code,
                m.wall.subsession.round_number,
                m.wall.node.network_id,
                m.wall.node.network.group_set.first().id_in_subsession,
                m.wall.node.network.nType,
                m.createdBy.bot,
                createdBy_code,
                m.createdBy.avatar.get_name(),
                m.createdBy.threshold,
                m.createdBy.position,
                m.wall.node.bot,
                wall_code,
                m.wall.node.avatar.get_name(),
                m.wall.node.threshold,
                m.wall.node.position,
                m.message,
                m.deleted,
                m.datetime,
            )
            rows.append(row)



        column_names = [
            'session.code',
            'subsession__round_number',
            'network_id',
            'network_position',
            'network_type',
            'createdBy__bot',
            'createdBy__code',
            'createdBy__avatar',
            'createdBy__threshold',
            'createdBy__position',
            'messageBox__node__bot',
            'messageBox__code',
            'messageBox__avatar',
            'messageBox__threshold',
            'messageBox__position',
            'message',
            'deleted',
            'datetime',
        ]

        writer = csv.writer(response)
        writer.writerows([column_names])
        writer.writerows(rows)

        return response

class NetworkExport(vanilla.View):

    url_name = 'main_network_export'
    url_pattern = '^main_network_export/$'
    display_name = 'Network export'

    def get(request, *args, **kwargs):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            'Network (accessed {}).csv'.format(
                datetime.date.today().isoformat()
            )
        )

        networks = Network.objects.order_by()
        rows = []
        counter = 1;

        for n in networks:
            nodes = n.getNodes()
            net_type = n.nType
            row = []
            row.append(counter)
            row.append(net_type)

            for node in nodes:
                row.append((node['image'].split("/",3)[3]).split("-")[0])
                row.append(node['label'].split(" ",1)[1])

            rows.append(row)
            counter += 1


        column_names = [
            'network',
            'network type',
            'node 1 bot',
            'node 1 threshold',
            'node 2 bot',
            'node 2 threshold',
            'node 3 bot',
            'node 3 threshold',
            'node 4 bot',
            'node 4 threshold',
            'node 5 bot',
            'node 5 threshold']
       

        writer = csv.writer(response)
        writer.writerows([column_names])
        writer.writerows(rows)

        return response
