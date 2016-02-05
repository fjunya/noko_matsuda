# -*- encoding: utf-8 -*-
import csv
import logging

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from participantgroup.forms import (DeleteForm, EditForm, ImportForm,
                                    ImportRowForm)
from participant.models import Participant, ParticipantGroup

logger = logging.getLogger('common')

PARTICIPANT_GROUPS_PER_PAGE = 20
EXPORT_FIELD_NAMES = ['group_name', 'info']
EXPORT_FILE_NAME = 'group.csv'

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def create(request):
    participants = Participant.objects.all()
    if request.method == 'POST':
        query = request.POST.copy()
        form = EditForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    participant_group = ParticipantGroup.objects.create(
                        group_name=d['group_name'],
                        info=d['info'])
                    for participant_id in d['participant']:
                        participant_group.participants.add(
                            Participant.objects.get(pk=participant_id))
                    participant_group.save()
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'participantgroup/complete.html',
                          {'message': u'端末グループを更新しました。'})
    else:
        form = EditForm()
    return render(
        request, 'participantgroup/edit.html',
        {'edit_type': 'create', 'form': form, 'participants': participants})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def delete(request):
    query = (request.POST.copy() if request.method == 'POST'
             else request.GET.copy())
    form = DeleteForm(query)
    participant_groups = None
    if form.is_valid():
        participant_group_ids = form.cleaned_data['participant_group_id']
        participant_groups = [ParticipantGroup.objects.get(pk=x) for x
                              in participant_group_ids]
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    map(lambda x: x.delete(), participant_groups)
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'participantgroup/complete.html',
                          {'message': u'端末グループを削除しました。'})
    return render(request, 'participantgroup/delete_confirm.html',
                  {'form': form, 'participant_groups': participant_groups})

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
    for participant_group in ParticipantGroup.objects.all():
        row = {
            'group_name': participant_group.group_name,
            'info': participant_group.info
        }
        row = {k: ('' if v is None else v) for k, v in row.items()}
        row = {k: unicode(v).encode('utf-8') for k, v in row.items()}
        writer.writerow(
            [row.get(x) or '' for x in EXPORT_FIELD_NAMES] +
            [unicode(x['display_name']).encode('utf-8') for x
             in participant_group.participants.values()])
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
                        dict_['participant'] = row[len(EXPORT_FIELD_NAMES):]
                        form = ImportRowForm(dict_)
                        if not form.is_valid():
                            row_errors = form.errors
                            raise ValidationError(None)
                        d = form.cleaned_data
                        participant_group = ParticipantGroup(
                            group_name=d['group_name'],
                            info=d['info'])
                        participant_group.save()
                        for display_name in d['participant']:
                            participant_group.participants.add(
                                Participant.objects.get(
                                    display_name=display_name))
            except Exception:
                logger.exception(None)
                return render(request, 'participantgroup/import.html',
                              {'form': import_form, 'row_errors': row_errors,
                               'row_num': row_num})
            return render(request, 'participantgroup/complete.html',
                          {'message': u'端末グループをインポートしました。'})
    else:
        import_form = ImportForm()
    return render(
        request, 'participantgroup/import.html', {'form': import_form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def list(request):
    participant_group_list = ParticipantGroup.objects.all()
    paginator = Paginator(participant_group_list, PARTICIPANT_GROUPS_PER_PAGE)
    page = request.GET.get('p')
    try:
        participant_groups = paginator.page(page)
    except PageNotAnInteger:
        participant_groups = paginator.page(1)
    except EmptyPage:
        participant_groups = paginator.page(paginator.num_pages)
    return render(request, 'participantgroup/listing.html',
                  {'participant_groups': participant_groups})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def update(request, participant_group_id=None):
    try:
        participant_group = \
            ParticipantGroup.objects.get(pk=participant_group_id)
    except ParticipantGroup.DoesNotExist:
        raise Http404(u'端末グループが存在しません。')

    participants = Participant.objects.all()
    if request.method == 'POST':
        query = request.POST.copy()
        form = EditForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    participant_group.group_name=d['group_name']
                    participant_group.info=d['info']
                    for participant_id in d['participant']:
                        participant_group.participants.add(
                            Participant.objects.get(pk=participant_id))
                    participant_group.save()
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'participantgroup/complete.html',
                          {'message': u'端末グループを更新しました。'})
    else:
        form = EditForm(initial={
            'group_name': participant_group.group_name,
            'info': participant_group.info,
            'participant': [x['id'] for x
                            in participant_group.participants.values('id')]
        })
    return render(
        request, 'participantgroup/edit.html',
        {'edit_type': 'update', 'form': form,
         'participant_group': participant_group, 'participants': participants})
