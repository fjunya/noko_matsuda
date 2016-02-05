# -*- encoding: utf-8 -*-
import calendar
import csv
from collections import defaultdict
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import arrow
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.http import Http404, HttpResponseBadRequest, HttpResponse
from django.shortcuts import redirect, render

from reserve.forms import ListAPIForm
from reserve.models import Conference, Resource

calendar.setfirstweekday(calendar.SUNDAY)

RESERVE_LISTING_API_RESPONSE_FIELDS = [
    {'name': 'reserveId', 'simple': True, 'detail': True},
    {'name': 'displayName', 'simple': True, 'detail': True},
    {'name': 'numericId', 'simple': True, 'detail': True},
    {'name': 'reserveDate', 'simple': True, 'detail': True},
    {'name': 'duration', 'simple': True, 'detail': True},
    {'name': 'endDate', 'simple': True, 'detail': True},
    {'name': 'bitrate', 'simple': True, 'detail': True},
    {'name': 'videoQuality', 'simple': False, 'detail': True},
    {'name': 'enterpriseMode', 'simple': False, 'detail': True},
    {'name': 'encryptFlg', 'simple': False, 'detail': True},
    {'name': 'selectedPartyNames', 'simple': True, 'detail': True},
    {'name': 'presentationMode', 'simple': True, 'detail': True},
    {'name': 'lecturer', 'simple': True, 'detail': True},
    {'name': 'sameLayoutMode', 'simple': True, 'detail': True},
    {'name': 'autoLayoutMode', 'simple': True, 'detail': True},
    {'name': 'layout', 'simple': True, 'detail': True},
    {'name': 'layoutPart0', 'simple': False, 'detail': True},
    {'name': 'layoutPart1', 'simple': False, 'detail': True},
    {'name': 'layoutPart2', 'simple': False, 'detail': True},
    {'name': 'layoutPart3', 'simple': False, 'detail': True},
    {'name': 'layoutPart4', 'simple': False, 'detail': True},
    {'name': 'layoutPart5', 'simple': False, 'detail': True},
    {'name': 'layoutPart6', 'simple': False, 'detail': True},
    {'name': 'layoutPart7', 'simple': False, 'detail': True},
    {'name': 'layoutPart8', 'simple': False, 'detail': True},
    {'name': 'layoutPart9', 'simple': False, 'detail': True},
    {'name': 'layoutPart10', 'simple': False, 'detail': True},
    {'name': 'layoutPart11', 'simple': False, 'detail': True},
    {'name': 'layoutPart12', 'simple': False, 'detail': True},
    {'name': 'layoutPart13', 'simple': False, 'detail': True},
    {'name': 'layoutPart14', 'simple': False, 'detail': True},
    {'name': 'layoutPart15', 'simple': False, 'detail': True},
    {'name': 'layoutPart16', 'simple': False, 'detail': True},
    {'name': 'layoutPart17', 'simple': False, 'detail': True},
    {'name': 'layoutPart18', 'simple': False, 'detail': True},
    {'name': 'layoutPart19', 'simple': False, 'detail': True},
    {'name': 'layoutPart20', 'simple': False, 'detail': True},
    {'name': 'reserveUserName', 'simple': False, 'detail': True},
    {'name': 'reserveUserDept', 'simple': False, 'detail': True},
    {'name': 'reserveUserMail', 'simple': False, 'detail': True},
    {'name': 'controlPassword', 'simple': False, 'detail': True},
    {'name': 'conferencePassword', 'simple': False, 'detail': True},
    {'name': 'enableRecordingFlg', 'simple': False, 'detail': True},
    {'name': 'reserveUserTel', 'simple': False, 'detail': True},
    {'name': 'reserveUserInfo', 'simple': False, 'detail': True},
    {'name': 'enterpriseProtocol', 'simple': False, 'detail': True}
]

def _indicate_resource(value):
   if value >= Resource.MAX_RESOURCES:
       return 'max'
   if value >= Resource.MAX_RESOURCES * 0.5:
       return 'warn'
   if value > 0:
       return 'fair'
   return '0'

def _resource_slots(hours):
    return [
        {'hour': hour, 'slots': [x + 6 * hour for x in range(6)]}
        for hour in hours
    ]

@login_required
def now_daily(request):
    now = datetime.now()
    return redirect('reserve_daily', ymd=now.strftime('%Y%m%d'), time=2)

@login_required
def now_monthly(request, ym=None):
    now = datetime.now()
    return redirect('reserve_monthly', ym=now.strftime('%Y%m'))

@login_required
def now_weekly(request, ym=None):
    now = datetime.now()
    return redirect('reserve_weekly', yw=now.strftime('%Y%U'), time=2)

@login_required
def daily(request, ymd=None, time=None):
    try:
        date = datetime.strptime(ymd, '%Y%m%d')
    except:
        raise Http404(u'日付が存在しません。')
    start = {'1': 0, '2': 8, '3': 14}[time]

    resources = Resource.objects.filter(date__gte=datetime.today()).\
                                 filter(date=date)

    slot_resource_statuses = [
        {
            'resource_status': _indicate_resource(x['sum']),
            'slot': x['slot']
        }
        for x in resources.values('date', 'slot').annotate(
            sum=Sum('conference__use_resource'))
    ]

    conferences = {
        resource.conference.id: {
            'conference': resource.conference,
        } for resource in resources
    }

    conference_resources = [
        {
            'conference': x['conference'],
            'resources': resources.filter(conference=x['conference'])
        }
        for x in conferences.values()
    ]

    pages = {
        'active_day_param': ymd,
        'month_param': date.strftime('%Y%m'),
        'next_day_param': (date + timedelta(days=1)).strftime('%Y%m%d'),
        'previous_day_param': (date + timedelta(days=-1)).strftime('%Y%m%d'),
        'week_param': date.strftime('%Y%U')
    }

    return render(
        request, 'reserve/daily.html', {
            'conference_resources': conference_resources,
            'date': date,
            'pages': pages,
            'resource_slots': _resource_slots(range(start, start + 10)),
            'slot_resource_statuses': slot_resource_statuses,
            'time_range': time
        })

@login_required
def monthly(request, ym=None):
    import logging
    logger = logging.getLogger('common')

    try:
        date_gte = datetime.strptime(ym, '%Y%m')
    except:
        raise Http404(u'日付が存在しません。')

    date_lt = date_gte + relativedelta(months=1)
    resources = Resource.objects.filter(date__gte=datetime.today()).\
                                 filter(date__gte=date_gte).\
                                 filter(date__lt=date_lt)

    tmp = defaultdict(dict)
    for x in resources.values('date', 'conference'):
       tmp[x['date']][x['conference']] = True
    date_reservations = [
        {'date': date, 'reservations': len(conferences.keys())}
        for date, conferences in tmp.items()
    ]

    pages = {
        'active_month_param': ym,
        'next_month_param':
        (date_gte + relativedelta(months=1)).strftime('%Y%m'),
        'previous_month_param':
        (date_gte + timedelta(days=-7)).strftime('%Y%m')
    }

    return render(
        request, 'reserve/monthly.html', {
            'calendar': calendar.monthcalendar(date_gte.year, date_gte.month),
            'date_gte': date_gte,
            'date_reservations': date_reservations,
            'holidays':  [datetime.strptime(x, '%Y-%m-%d') for x
                          in settings.HOLIDAYS.keys()],
            'now': datetime.now(),
            'pages': pages
        })

@login_required
def weekly(request, yw=None, time=None):
    try:
        0 <= int(yw[4:6]) < 53
        date_gte = datetime.strptime(yw + '0', '%Y%U%w')
    except:
        raise Http404(u'日付が存在しません。')
    start = {'1': 0, '2': 8, '3': 14}[time]

    date_lt = date_gte + timedelta(days=7)
    resources = Resource.objects.filter(date__gte=datetime.today()).\
                                 filter(date__gte=date_gte).\
                                 filter(date__lt=date_lt)

    slot_resource_statuses = [
        {
            'date': x['date'],
            'resource_status': _indicate_resource(x['sum']),
            'slot': x['slot']
        }
        for x in resources.values('date', 'slot').annotate(
            sum=Sum('conference__use_resource'))
    ]

    pages = {
        'active_week_param': yw,
        'month_param': date_gte.strftime('%Y%m'),
        'next_week_param': (date_gte + timedelta(days=7)).strftime('%Y%U'),
        'previous_week_param':
        (date_gte + timedelta(days=-7)).strftime('%Y%U'),
        'week_param': date_gte.strftime('%Y%U')
    }

    return render(
        request, 'reserve/weekly.html', {
            'date_gte': date_gte,
            'pages': pages,
            'resource_slots': _resource_slots(range(start, start + 10)),
            'resource_slots_set': [
                {
                    'date': date_gte + timedelta(days=day),
                    'items': _resource_slots(range(start, start + 10))
                }
                for day in range(7)
            ],
            'slot_resource_statuses': slot_resource_statuses,
            'time_range': time
        })

def list_api(request):
    query = (request.POST.copy() if request.method == 'POST'
             else request.GET.copy())
    form = ListAPIForm(query)
    if not form.is_valid():
        return HttpResponseBadRequest()

    conferences = Conference.objects.all()
    date_from = form.cleaned_data.get('dateFrom')
    if date_from:
        conferences = conferences.filter(startTime__gte=date_from)
    date_to = form.cleaned_data.get('dateTo')
    if date_to:
        conferences = conferences.filter(
            startTime__lt=date_to + timedelta(days=1))

    view = form.cleaned_data.get('view') or 'simple'
    fields = [x['name'] for x in RESERVE_LISTING_API_RESPONSE_FIELDS
              if x[view]]
    response = HttpResponse(content_type='text/plain')
    writer = csv.writer(response, delimiter=',')
    if False:
        writer.writerow(fields)

    date_format = \
        form.cleaned_data.get('dateFormat') or 'YYYY-MM-DD HH:mm:ss.SSS'

    for conference in conferences:
        row = {}
        row['reserveId'] = conference.id
        row['displayName'] = conference.title
        row['numericId'] = conference.mcu_conferenceNo
        row['reserveDate'] = arrow.get(conference.startTime
                                       ).format(date_format)
        row['duration'] = (conference.endTime - conference.startTime
                           ).seconds / 60
        if conference.endTime > datetime.now():
            row['endDate'] = ''
        else:
            row['endDate'] = arrow.get(conference.endTime).format(date_format)
        row['bitrate'] = conference.bandwidth
        row['videoQuality'] = conference.videoQuality
        row['encryptFlg'] = conference.encrypted
        row['selectedPartyNames'] = \
            ';'.join([x['display_name'].replace('\\', '\\\\').replace(';', '\\;')
                      for x in conference.participants.values()])
        row['presentationMode'] = conference.layout_mode == 'presentationMode'
        row['lecturer'] = conference.presenter
        row['sameLayoutMode'] = conference.layout_mode == 'sameLayout'
        row['autoLayoutMode'] = conference.layout_mode == 'autoLayout'
        # TODO
        row['layout'] = conference.layout_no
        # TODO
        #row['layoutPart0'] =
        row['layoutPart1'] = conference.pane1 
        row['layoutPart2'] = conference.pane2
        row['layoutPart3'] = conference.pane3
        row['layoutPart4'] = conference.pane4
        row['layoutPart5'] = conference.pane5
        row['layoutPart6'] = conference.pane6
        row['layoutPart7'] = conference.pane7
        row['layoutPart8'] = conference.pane8
        row['layoutPart9'] = conference.pane9
        row['layoutPart10'] = conference.pane10
        row['layoutPart11'] = conference.pane11
        row['layoutPart12'] = conference.pane12
        row['layoutPart13'] = conference.pane13
        row['layoutPart14'] = conference.pane14
        row['layoutPart15'] = conference.pane15
        row['layoutPart16'] = conference.pane16
        # TODO
        #row['layoutPart17'] = conference.pane17
        #row['layoutPart18'] = conference.pane18
        #row['layoutPart19'] = conference.pane19
        #row['layoutPart20'] = conference.pane20
        row['reserveUserName'] = conference.userName
        row['reserveUserDept'] = conference.department 
        row['reserveUserMail'] = conference.mail
        row['controlPassword'] = conference.controlPassword
        row['conferencePassword'] = conference.conferencePassword
        # TODO
        row['enableRecordingFlg'] = conference.recording
        row['reserveUserTel'] = conference.tel
        row['reserveUserInfo'] = conference.description
        row['enterpriseProtocol'] = conference.h239
        row = {k: ('' if v is None else v) for k, v in row.items()}
        row = {k: unicode(v).encode('utf-8') for k, v in row.items()
               if k in fields}
        writer.writerow([row.get(x) or '' for x in fields])
    return response
