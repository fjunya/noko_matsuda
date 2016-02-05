# -*- encoding: utf-8 -*-
import csv
import logging
import subprocess

from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.http import (Http404, HttpResponse, HttpResponseBadRequest,
                         JsonResponse)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from participant.forms import (DeleteForm, EditForm, ImportForm, ImportRowForm,
                               ListAPIForm)
from participant.models import Participant
from stormysapphire.decorators import login_required

logger = logging.getLogger('common')

PARTICIPANTS_PER_PAGE = 50
EXPORT_FIELD_NAMES = [
    'display_name', 'direction', 'type', 'ip_address', 'alias_name',
    'alias_type', 'model', 'audio_only_flg', 'info', 'bitrate',
    'software_version', 'phone1', 'video_protocol', 'cascade_role',
    'sip_address', 'sip_address_type'
]
EXPORT_FILE_NAME = 'terminal.csv'
PARTICIPANT_LISTING_API_RESPONSE_FIELDS = [
    'terminalId', 'displayName', 'direction', 'type', 'ipAddress', 'aliasName',
    'aliasType', 'model', 'hdFlg', 'audioOnlyFlg', 'info', 'bitRate',
    'softwareVersion', 'phone1', 'videoProtocol', 'cascadeRole', 'sipAddress',
    'sipAddressType', 'category', 'maxResolution'
]

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def create(request):
    if request.method == 'POST':
        query = request.POST.copy()
        form = EditForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    ip_address = '.'.join([d[x] for x
                                           in ['ip_address1', 'ip_address2',
                                               'ip_address3', 'ip_address4']])
                    participant = Participant(
                        display_name=d['display_name'],
                        direction=d['direction'],
                        type=d['type'],
                        ip_address=ip_address,
                        alias_name=d['alias_name'],
                        alias_type=d['alias_type'],
                        model=d['model'],
                        audio_only_flg=d['audio_only_flg'],
                        info=d['info'],
                        bitrate=d['bitrate'],
                        software_version=d['software_version'],
                        phone1=d['phone1'],
                        video_protocol=d['video_protocol'],
                        cascade_role=d['cascade_role'],
                        sip_address=d['sip_address'],
                        sip_address_type=d['sip_address_type'])
                    participant.save()
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'participant/complete.html',
                          {'message': u'端末を更新しました。'})
    else:
        form = EditForm()
    return render(request, 'participant/edit.html',
                  {'edit_type': 'create', 'form': form})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def delete(request):
    query = (request.POST.copy() if request.method == 'POST'
             else request.GET.copy())
    form = DeleteForm(query)
    participants = None
    if form.is_valid():
        participant_ids = form.cleaned_data['participant_id']
        participants = [Participant.objects.get(pk=x) for x in participant_ids]
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    map(lambda x: x.delete(), participants)
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'participant/complete.html',
                          {'message': u'端末を削除しました。'})
    return render(request, 'participant/delete_confirm.html',
                  {'form': form, 'participants': participants})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename="{}"'.format(EXPORT_FILE_NAME)
    writer = csv.writer(response, delimiter=',')
    if False:
        writer.writerow(EXPORT_FIELD_NAMES)
    for participant in Participant.objects.all():
        row = {
            'display_name': participant.display_name,
            'direction': participant.direction,
            'type': participant.type,
            'ip_address': participant.ip_address,
            'alias_name': participant.alias_name,
            'alias_type': participant.alias_type,
            'model': participant.model,
            'audio_only_flg': participant.audio_only_flg,
            'info': participant.info,
            'bitrate': participant.bitrate,
            'software_version': participant.software_version,
            'phone1': participant.phone1,
            'video_protocol': participant.video_protocol,
            'cascade_role': participant.cascade_role,
            'sip_address': participant.sip_address,
            'sip_address_type': participant.sip_address_type,
        }
        for x in ('audio_only_flg',):
            if row[x] is True:
                row[x] = str(int(row[x]))
            else:
                row[x] = ''
        row = {k: ('' if v is None else v) for k, v in row.items()}
        row = {k: unicode(v).encode('utf-8') for k, v in row.items()}
        writer.writerow([row.get(x) or '' for x in EXPORT_FIELD_NAMES])
    return response

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def import_(request):
    if request.method == 'POST':
        import_form = ImportForm(request.POST.copy(), request.FILES)
        if import_form.is_valid():
            try:
                row_num = 1
                row_errors = None
                with transaction.atomic():
                    for row in csv.reader(import_form.cleaned_data['file']):
                        row_num += 1
                        dict_ = dict(zip(EXPORT_FIELD_NAMES, row))
                        form = ImportRowForm(dict_)
                        if not form.is_valid():
                            row_errors = form.errors
                            raise ValidationError(None)
                        d = form.cleaned_data
                        participant = Participant(
                            display_name=d['display_name'],
                            direction=d['direction'],
                            type=d['type'],
                            ip_address=d['ip_address'],
                            alias_name=d['alias_name'],
                            alias_type=d['alias_type'],
                            model=d['model'],
                            audio_only_flg=d['audio_only_flg'],
                            info=d['info'],
                            bitrate=d['bitrate'] or None,
                            software_version=d['software_version'],
                            phone1=d['phone1'],
                            video_protocol=d['video_protocol'],
                            cascade_role=d['cascade_role'],
                            sip_address=d['sip_address'],
                            sip_address_type=d['sip_address_type'])
                        participant.save()
            except Exception:
                logger.exception(None)
                return render(
                    request, 'participant/import.html',
                    {'form': import_form, 'row_errors': row_errors,
                     'row_num': row_num})
            return render(request, 'participant/complete.html',
                          {'message': u'端末をインポートしました。'})
    else:
        import_form = ImportForm()
    return render(request, 'participant/import.html', {'form': import_form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def list(request):
    participant_list = Participant.objects.all()
    paginator = Paginator(participant_list, PARTICIPANTS_PER_PAGE)
    page = request.GET.get('p')
    try:
        participants = paginator.page(page)
    except PageNotAnInteger:
        participants = paginator.page(1)
    except EmptyPage:
        participants = paginator.page(paginator.num_pages)
    return render(
        request, 'participant/listing.html', {'participants': participants})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def update(request, participant_id=None):
    try:
        participant = Participant.objects.get(pk=participant_id)
    except Participant.DoesNotExist:
        raise Http404(u'端末が存在しません。')

    if request.method == 'POST':
        query = request.POST.copy()
        form = EditForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    ip_address = '.'.join(
                        [d[x] for x in ['ip_address1', 'ip_address2',
                                        'ip_address3', 'ip_address4']])
                    participant.display_name=d['display_name']
                    participant.direction=d['direction']
                    participant.type=d['type']
                    participant.ip_address=ip_address
                    participant.alias_name=d['alias_name']
                    participant.alias_type=d['alias_type']
                    participant.model=d['model']
                    participant.audio_only_flg=d['audio_only_flg']
                    participant.info=d['info']
                    participant.bitrate=d['bitrate']
                    participant.software_version=d['software_version']
                    participant.phone1=d['phone1']
                    participant.video_protocol=d['video_protocol']
                    participant.cascade_role=d['cascade_role']
                    participant.sip_address=d['sip_address']
                    participant.sip_address_type=d['sip_address_type']
                    participant.save()
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'participant/complete.html',
                          {'message': u'端末を更新しました。'})
    else:
        ip_address1, ip_address2, ip_address3, ip_address4 = \
            participant.ip_address.split('.')
        form = EditForm(initial={
            'display_name': participant.display_name,
            'direction': participant.direction,
            'type': participant.type,
            'ip_address1': ip_address1,
            'ip_address2': ip_address2,
            'ip_address3': ip_address3,
            'ip_address4': ip_address4,
            'alias_name': participant.alias_name,
            'alias_type': participant.alias_type,
            'model': participant.model,
            'audio_only_flg': participant.audio_only_flg,
            'info': participant.info,
            'bitrate': participant.bitrate,
            'software_version': participant.software_version,
            'phone1': participant.phone1,
            'video_protocol': participant.video_protocol,
            'cascade_role': participant.cascade_role,
            'sip_address': participant.sip_address,
            'sip_address_type': participant.sip_address_type,
        })
    return render(
        request, 'participant/edit.html',
        {'edit_type': 'update', 'form': form, 'participant': participant})

def list_api(request):
    query = (request.POST.copy() if request.method == 'POST'
             else request.GET.copy())
    form = ListAPIForm(query)
    if not form.is_valid():
        return HttpResponseBadRequest()

    participants = Participant.objects.all()

    fields = PARTICIPANT_LISTING_API_RESPONSE_FIELDS
    response = HttpResponse(content_type='text/plain')
    writer = csv.writer(response, delimiter=',')
    if False:
        writer.writerow(fields)

    for participant in participants:
        # TODO
        row = {
            'terminalId': participant.id,
            'displayName': participant.display_name,
            'direction': participant.direction,
            'type': participant.type,
            'ipAddress': participant.ip_address,
            'aliasName': participant.alias_name,
            'aliasType': participant.alias_type,
            'model': participant.model,
            #'hdFlg': 
            'audioOnlyFlg': participant.audio_only_flg,
            'info': participant.info,
            'bitRate': participant.bitrate,
            'softwareVersion': participant.software_version,
            'phone1': participant.phone1,
            'videoProtocol': participant.video_protocol,
            'cascadeRole': participant.cascade_role,
            'sipAddress': participant.sip_address,
            'sipAddressType': participant.sip_address_type,
            #'category':
            #'maxResolution': 
        }
        row = {k: ('' if v is None else v) for k, v in row.items()}
        row = {k: unicode(v).encode('utf-8') for k, v in row.items()}
        writer.writerow([row.get(x) or '' for x in fields])
    return response

@user_passes_test(lambda u: u.is_staff)
def ping_api(request, host=None):
    ret = subprocess.call(['ping', '-c', '1', host],
                          stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    success = False
    if ret == 0:
        success = True
    return JsonResponse({'success': success})
