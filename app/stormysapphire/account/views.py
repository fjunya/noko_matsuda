# -*- encoding: utf-8 -*-
import csv
from datetime import datetime
import logging

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import transaction
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from account.forms import (CreateForm, DeleteForm, ImportForm, ImportRowForm,
                           UpdateForm)
from account.models import Account, AccountGroup
from stormysapphire.decorators import login_required

logger = logging.getLogger('common')

ACCOUNTS_PER_PAGE = 20
EXPORT_FIELD_NAMES = [
    'username', 'role', 'last_name', 'first_name', 'email', 'dept', 'tel',
    'info', 'date_from', 'date_to', 'no_validity', 'reserve_days',
    'no_reserve_days'
]
EXPORT_FILE_NAME = 'account.csv'

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def create(request):
    account_groups = AccountGroup.objects.all()
    if request.method == 'POST':
        query = request.POST.copy()
        form = CreateForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    user = User.objects.create_user(
                        d['username'],
                        d['email'],
                        d['password'])
                    user.is_staff = bool(d['role'])
                    user.first_name = d['first_name']
                    user.last_name = d['last_name']
                    user.save()

                    account = Account(
                        user=user,
                        dept=d['dept'],
                        tel=d['tel'],
                        date_from=d['date_from'],
                        date_to=d['date_to'],
                        no_validity=d['no_validity'],
                        reserve_days=d['reserve_days'],
                        no_reserve_days=d['no_reserve_days'],
                        info=d['info'])
                    account.save()
                    for account_group_id in d['account_group']:
                        account.account_groups.add(
                            AccountGroup.objects.get(pk=accountgroup_id))
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'account/complete.html',
                          {'message': u'アカウントを追加しました。'})
    else:
        form = CreateForm()
    return render(
        request, 'account/edit.html',
        {'account_groups': account_groups, 'edit_type': 'create',
         'form': form})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def delete(request):
    query = (request.POST.copy() if request.method == 'POST'
             else request.GET.copy())
    form = DeleteForm(query)
    accounts, users = None, None
    if form.is_valid():
        user_ids = form.cleaned_data['user_id']
        accounts = [Account.objects.get(user_id=x) for x in user_ids]
        users = [User.objects.get(pk=x) for x in user_ids]
        if request.method == 'POST':
            try:
                with transaction.atomic():
                    map(lambda x: x.delete(), accounts)
                    map(lambda x: x.delete(), users)
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'account/complete.html',
                          {'message': u'アカウントを削除しました。'})
    return render(
        request, 'account/delete_confirm.html', {'form': form, 'users': users})

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
    for account in Account.objects.exclude(user__isnull=True):
        row = {
            'username': account.user.username,
            'email': account.user.email,
            'role': account.user.is_staff,
            'first_name': account.user.first_name,
            'last_name': account.user.last_name,
            'dept': account.dept,
            'tel': account.tel,
            'date_from': account.date_from,
            'date_to': account.date_to,
            'no_validity': account.no_validity,
            'reserve_days': account.reserve_days,
            'no_reserve_days': account.no_reserve_days,
            'info': account.info
        }
        row = {k: ('' if v is None else v) for k, v in row.items()}
        for x in ('role',):
            if type(row[x]) == bool:
                row[x] = str(int(row[x]))
        for x in ('date_from', 'date_to'):
            if type(row[x]) == datetime:
                row[x] = row[x].strftime('%Y/%m/%d')
        for x in ('no_validity', 'no_reserve_days'):
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
                        user = User.objects.create_user(
                            d['username'],
                            d['email'],
                            d['username'])
                        user.is_staff = bool(d['role'])
                        user.first_name = d['first_name']
                        user.last_name = d['last_name']
                        user.save()

                        account = Account(
                            user=user,
                            dept=d['dept'],
                            tel=d['tel'],
                            date_from=d['date_from'],
                            date_to=d['date_to'],
                            no_validity=d['no_validity'],
                            reserve_days=d['reserve_days'],
                            no_reserve_days=d['no_reserve_days'],
                            info=d['info'])
                        account.save()
            except Exception:
                logger.exception(None)
                return render(request, 'account/import.html',
                              {'form': import_form, 'row_errors': row_errors,
                               'row_num': row_num})
            return render(request, 'account/complete.html',
                          {'message': u'アカウントをインポートしました。'})
    else:
        import_form = ImportForm()
    return render(request, 'account/import.html', {'form': import_form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def list(request):
    account_list = Account.objects.exclude(user__isnull=True)
    paginator = Paginator(account_list, ACCOUNTS_PER_PAGE)
    page = request.GET.get('p')
    try:
        accounts = paginator.page(page)
    except PageNotAnInteger:
        accounts = paginator.page(1)
    except EmptyPage:
        accounts = paginator.page(paginator.num_pages)
    return render(request, 'account/listing.html', {'accounts': accounts})

@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_staff)
def update(request, user_id=None):
    try:
        user = User.objects.get(pk=user_id)
        account = Account.objects.get(user__id=user_id)
    except (User.DoesNotExist, Account.DoesNotExist):
        raise Http404(u'ユーザが存在しません。')

    account_groups = AccountGroup.objects.all()
    if request.method == 'POST':
        query = request.POST.copy()
        form = UpdateForm(query)
        if form.is_valid():
            try:
                with transaction.atomic():
                    d = form.cleaned_data
                    user.email = d['email']
                    if d['password']:
                        user.set_password(d['password'])
                    user.is_staff = bool(d['role'])
                    user.first_name = d['first_name']
                    user.last_name = d['last_name']
                    user.save()

                    account.dept = d['dept']
                    account.tel = d['tel']
                    account.date_from = d['date_from']
                    account.date_to = d['date_to']
                    account.no_validity = d['no_validity']
                    account.reserve_days = d['reserve_days']
                    account.no_reserve_days = d['no_reserve_days']
                    account.info = d['info']
                    account.account_groups.clear()
                    for account_group_id in d['account_group']:
                        account.account_groups.add(
                            AccountGroup.objects.get(pk=account_group_id))
                    account.save()
            except Exception:
                logger.exception(None)
                raise 
            return render(request, 'account/complete.html',
                          {'message': u'アカウントを更新しました。'})
    else:
        form = UpdateForm(initial={
            'username': account.user.username,
            'email': account.user.email,
            'role': int(account.user.is_staff),
            'first_name': account.user.first_name,
            'last_name': account.user.last_name,
            'dept': account.dept,
            'tel': account.tel,
            'date_from': account.date_from,
            'date_to': account.date_to,
            'no_validity': account.no_validity,
            'reserve_days': account.reserve_days,
            'no_reserve_days': account.no_reserve_days,
            'info': account.info,
            'account_group': [x['id'] for x in
                              account.account_groups.values('id')],
        })
    return render(request, 'account/edit.html',
                  {'account': account, 'account_groups': account_groups,
                   'edit_type': 'update', 'form': form})
