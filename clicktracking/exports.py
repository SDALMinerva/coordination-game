import csv
import datetime

from django.http import HttpResponse

import vanilla

from .models import Click


class ClickExport(vanilla.View):

    url_name = 'clicktracking_click_export'
    url_pattern = '^clicktracking_click_export/$'
    display_name = 'Clicktracking export'

    def get(request, *args, **kwargs):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(
            'Clicktracking (accessed {}).csv'.format(
                datetime.date.today().isoformat()
            )
        )

        column_names = [
            'session__code',
            'participant__code',
            'participant_id',
            'page',
            'element',
            'timestamp'
        ]

        rows = Click.objects.order_by('timestamp').values_list(*column_names)

        writer = csv.writer(response)
        writer.writerows([column_names])
        writer.writerows(rows)

        return response
