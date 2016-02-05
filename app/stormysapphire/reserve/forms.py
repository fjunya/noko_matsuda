# -*- encoding: utf-8 -*-
import logging

import arrow
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

logger = logging.getLogger('common')

FORMAT_CHOICES = (('csv', 'csv'),)
PARTY_TYPE_CHOICES = (('id', 'id'), ('ip', 'ip'))
VIEW_CHOICES = (('simple', 'simple'), ('detail', 'detail'))

def validate_date_format(value):
    try:
        value = value.replace('yyyy', 'YYYY').\
                      replace('dd', 'DD')
        arrow.now().format(value)
    except:
        raise ValidationError(u'不正な日時フォーマットです。')


class ListAPIForm(forms.Form):
    apiKey = forms.CharField(
        max_length=40, required=True,
        validators=[
            RegexValidator(regex='^{}$'.format(settings.API_KEY),
                           message=u'不正なキーです。')],
       widget=forms.TextInput(attrs={'size': 40}))
    dateFrom = forms.DateField(
        input_formats=['%Y%m%d'], required=False,
        widget=forms.DateInput(attrs={'size': 8}, format='%Y%m%d'))
    dateTo = forms.DateField(
        input_formats=['%Y%m%d'], required=False,
        widget=forms.DateInput(attrs={'size': 8}, format='%Y%m%d'))
    partyType = forms.ChoiceField(PARTY_TYPE_CHOICES, required=False)
    view = forms.ChoiceField(VIEW_CHOICES, required=False)
    dateFormat = forms.CharField(
        max_length=128, required=False, validators=[validate_date_format],
        widget=forms.TextInput(attrs={'size': 128}))
    format = forms.ChoiceField(FORMAT_CHOICES, required=False)
 
    def clean_dateFormat(self):
        value = self.cleaned_data['dateFormat']
        value = value.replace('yyyy', 'YYYY').\
                      replace('dd', 'DD')
        return value
