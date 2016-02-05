# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django import forms

from account.models import AccountGroup

ROLE_CHOICES = ((0, u'ユーザー'), (1, u'管理者'))


class EditForm(forms.Form):
    username = forms.CharField(
        max_length=16, required=True,
        validators=[
            RegexValidator(regex='^[A-z0-9\-]+$',
                           message=u'半角英数字のみ使用可能です。')],
       widget=forms.TextInput(attrs={'size': 16}))
    last_name = forms.CharField(
        max_length=32, required=True,
        widget=forms.TextInput(attrs={'placeholder': u'姓', 'size': 32}))
    first_name = forms.CharField(
        max_length=32, required=True,
        widget=forms.TextInput(attrs={'placeholder': u'名', 'size': 32}))
    password = forms.CharField(max_length=16,
                               widget=forms.PasswordInput(attrs={'size': 16}))
    password2 = forms.CharField(max_length=16,
                                widget=forms.PasswordInput(attrs={'size': 16}))
    email = forms.EmailField(max_length=64, required=False,
                             widget=forms.EmailInput(attrs={'size': 64}))
    role = forms.TypedChoiceField(choices=ROLE_CHOICES, coerce=int,
                                  required=True)
    dept = forms.CharField(max_length=64, required=False,
                           widget=forms.TextInput(attrs={'size': 64}))
    tel = forms.CharField(
        max_length=32, required=False,
        validators=[
            RegexValidator(
                regex='^[0-9\-]+$',
                message=u'半角数字と半角ハイフンのみ使用可能です。')],
        widget=forms.TextInput(attrs={'size': 32}))
    date_from = forms.DateField(
        input_formats=['%Y/%m/%d'], required=False,
        widget=forms.DateInput(attrs={'size': 10}, format='%Y/%m/%d'))
    date_to = forms.DateField(
        input_formats=['%Y/%m/%d'], required=False,
        widget=forms.DateInput(attrs={'size': 10}, format='%Y/%m/%d'))
    no_validity = forms.BooleanField(initial=True, required=False)
    reserve_days = forms.IntegerField(max_value=999, min_value=1,
                                      required=False)
    no_reserve_days = forms.BooleanField(initial=True, required=False)
    info = forms.CharField(max_length=64, required=False,
                           widget=forms.TextInput(attrs={'size': 64}))

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['account_group'] = forms.TypedMultipleChoiceField(
            choices=tuple((x['id'], x['name']) for x
                           in AccountGroup.objects.values()),
            required=False)

    def clean(self):
        cleaned_data = super(EditForm, self).clean()

        if cleaned_data.get('password') != cleaned_data.get('password2'):
            self.add_error('password2', u'パスワードが一致しません。')

        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')
        no_validity = cleaned_data.get('no_validity')
        if not (date_from or date_to or no_validity):
            self.add_error('no_validity', u'いずれかのフィールドは必須です。')
        if no_validity:
            if date_from or date_to:
                self.add_error('no_validity', u'いずれかのみ入力します。')
        else:
            if date_from and date_to and (date_from > date_to):
                self.add_error(
                    'no_validity', u'期間を正しく入力してください。')

        reserve_days = cleaned_data.get('reserve_days')
        no_reserve_days = cleaned_data.get('no_reserve_days')
        if not (reserve_days or no_reserve_days):
            self.add_error(
                'no_reserve_days', u'いずれかのフィールドは必須です。')
        if reserve_days and no_reserve_days:
            self.add_error('no_reserve_days', u'いずれかのみ入力します。')


class CreateForm(EditForm):
    pass


class UpdateForm(EditForm):
    password = forms.CharField(max_length=16, required=False,
                               widget=forms.PasswordInput(attrs={'size': 16}))
    password2 = forms.CharField(max_length=16, required=False,
                                widget=forms.PasswordInput(attrs={'size': 16}))


class DeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['user_id'] = forms.TypedMultipleChoiceField(
            choices=tuple((x['id'], x['username']) for x
                           in User.objects.values('id', 'username')),
            required=True)


class ImportForm(forms.Form):
    file = forms.FileField()


class ImportRowForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        validators=[
            RegexValidator(regex='^[A-z0-9\-]+$',
                           message=u'半角英数字のみ使用可能です。')],
        required=True)
    last_name = forms.CharField(max_length=32, required=True)
    first_name = forms.CharField(max_length=32, required=True)
    email = forms.EmailField(max_length=64, required=False)
    role = forms.TypedChoiceField(choices=ROLE_CHOICES, coerce=int,
                                  required=True)
    dept = forms.CharField(max_length=64, required=False)
    tel = forms.CharField(
        max_length=32, required=False,
        validators=[
            RegexValidator(
                regex='^[0-9\-]+$',
                message=u'半角数字と半角ハイフンのみ使用可能です。')])
    date_from = forms.DateField(input_formats=['%Y/%m/%d'], required=False)
    date_to = forms.DateField(input_formats=['%Y/%m/%d'], required=False)
    no_validity = forms.BooleanField(initial=True, required=False)
    reserve_days = forms.IntegerField(max_value=999, min_value=1,
                                      required=False)
    no_reserve_days = forms.BooleanField(initial=True, required=False)
    info = forms.CharField(max_length=64, required=False)

    def clean(self):
        cleaned_data = super(ImportRowForm, self).clean()

        date_from = cleaned_data.get('date_from')
        date_to = cleaned_data.get('date_to')
        no_validity = cleaned_data.get('no_validity')
        if not (date_from or date_to or no_validity):
            self.add_error('no_validity', u'いずれかのフィールドは必須です。')
        if no_validity:
            if date_from or date_to:
                self.add_error('no_validity', u'いずれかのみ入力します。')
        else:
            if date_from and date_to and (date_from > date_to):
                self.add_error(
                    'no_validity', u'期間を正しく入力してください。')

        reserve_days = cleaned_data.get('reserve_days')
        no_reserve_days = cleaned_data.get('no_reserve_days')
        if not (reserve_days or no_reserve_days):
            self.add_error(
                'no_reserve_days', u'いずれかのフィールドは必須です。')
        if reserve_days and no_reserve_days:
            self.add_error('no_reserve_days', u'いずれかのみ入力します。')
