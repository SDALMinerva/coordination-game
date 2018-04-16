import csv
import datetime

from django.http import HttpResponse

import vanilla

from .models import Message


class MessageExport(vanilla.View):

    url_name = 'main_message_export'
    url_pattern = '^main_message_export/$'
    display_name = 'Sent Messages export'

    def get(request, *args, **kwargs):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            'Messages (accessed {}).csv'.format(
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
