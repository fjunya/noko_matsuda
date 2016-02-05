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

from accountgroup.forms import DeleteForm, EditForm, ImportForm, ImportRowForm
from account.models import Account, AccountGroup

logger = logging.getLogger('common')

ACCOUNT_GROUPS_PER_PAGE = 20
EXPORT_FIELD_NAMES = ['name', 'info']
EXPORT_FILE_NAME = 'accountGroup.csv'

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def create(request):
    accounts = Account.objects.all()
    if request.method == 'POST':
        query = request.POST.copy()
        form = EditForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    account_group = AccountGroup(
                        name=d['name'],
                        info=d['info'])
                    account_group.save()
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'accountgroup/complete.html',
                          {'message': u'アカウントグループを追加しました。'})
    else:
        form = EditForm()
    return render(request, 'accountgroup/edit.html',
                  {'accounts': accounts, 'edit_type': 'create', 'form': form})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def delete(request):
    query = (request.POST.copy() if request.method == 'POST'
             else request.GET.copy())
    form = DeleteForm(query)
    account_groups = None
    if form.is_valid():
        account_group_ids = form.cleaned_data['account_group_id']
        account_groups = [AccountGroup.objects.get(pk=x) for x
                          in account_group_ids]
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    map(lambda x: x.delete(), account_groups)
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'accountgroup/complete.html',
                          {'message': u'アカウントグループを削除しました。'})
    return render(request, 'accountgroup/delete_confirm.html',
                  {'account_groups': account_groups, 'form': form})

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
    for account_group in AccountGroup.objects.all():
        row = {
            'name': account_group.name,
            'info': account_group.info
        }
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
                        account_group = AccountGroup(
                           name=d['name'],
                           info=d['info'])
                        account_group.save()
            except Exception:
                logger.exception(None)
                return render(request, 'accountgroup/import.html',
                              {'form': import_form, 'row_errors': row_errors,
                               'row_num': row_num})
            return render(
                request, 'accountgroup/complete.html',
                {'message': u'アカウントグループをインポートしました。'})
    else:
        import_form = ImportForm()
    return render(request, 'accountgroup/import.html', {'form': import_form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def list(request):
    account_group_list = AccountGroup.objects.all()
    paginator = Paginator(account_group_list, ACCOUNT_GROUPS_PER_PAGE)
    page = request.GET.get('p')
    try:
        account_groups = paginator.page(page)
    except PageNotAnInteger:
        account_groups = paginator.page(1)
    except EmptyPage:
        account_groups = paginator.page(paginator.num_pages)
    return render(request, 'accountgroup/listing.html',
                  {'account_groups': account_groups})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def update(request, account_group_id=None):
    try:
        account_group = AccountGroup.objects.get(pk=account_group_id)
    except AccountGroup.DoesNotExist:
        raise Http404(u'アカウントグループが存在しません。')

    if request.method == 'POST':
        query = request.POST.copy()
        form = EditForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    account_group.name=d['name']
                    account_group.info=d['info']
                    account_group.save()
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'accountgroup/complete.html',
                          {'message': u'アカウントグループを更新しました。'})
    else:
        form = EditForm(initial={'name': account_group.name,
                                 'info': account_group.info})
    return render(request, 'accountgroup/edit.html',
                  {'account_group': account_group, 'edit_type': 'update',
                   'form': form})
