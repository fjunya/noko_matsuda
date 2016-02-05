# -*- encoding: utf-8 -*-
from django.conf import settings
from django.core.validators import RegexValidator
from django import forms

from participant.models import Participant, ParticipantGroup

ALIAS_TYPE_CHOICES = (
    ('323_id', 'H.323-ID'), ('e164', 'E164'), ('url_id', 'URL-ID'),
    ('email_id', 'Email-ID'), ('party_number', u'参加端末番号')
)
BITRATE_CHOICES = (
    (None, u'自動'), (128, '128Kbps'), (192, '192Kbps'), (256, '256Kbps'),
    (384, '384Kbps'), (512, '512Kbps'), (768, '768Kbps'), (1024, '1024Kbps'),
    (1152, '1152Kbps'), (1472, '1472Kbps'), (1536, '1536Kbps'),
    (1920, '1920Kbps'), (4096, '4096Kbps')
)
CASCADE_ROLE_CHOICES = (
    ('none', u'なし'), ('master', 'Master'), ('slave', 'Slave')
)
DIRECTION_CHOICES = (('dial_in', 'Dial in'), ('dial_out', 'Dial out'))
MODEL_CHOICES = (
    ('', u'指定なし'), ('hdx9000', 'HDX 9000'),
    ('hdx9001', 'HDX 9001(SD)'), ('hdx8000', 'HDX 8000'),
    ('hdx8006', 'HDX 8006(1080p)'), ('hdx7000', 'HDX 7000'),
    ('hdx7001', 'HDX 7001(SD)'), ('hdx6000', 'HDX 6000'),
    ('hdx4000', 'HDX 4000'), ('hdx4001', 'HDX 4001(SD)'),
    ('vsx8000', 'VSX 8000'), ('vsx7000', 'VSX 7000'),
    ('vsx6000', 'VSX 6000'), ('vsx5000', 'VSX 5000'),
    ('vsx3000', 'VSX 3000'), ('v700', 'V700'), ('v500', 'V500'),
    ('pvx', 'PVX'), ('pvx_h264', 'PVX(H.264)'), ('other_hd', u'その他(HD)'),
    ('other_sd', u'その他(SD)') 
)
SIP_ADDRESS_TYPE_CHOICES = (
    ('uri_type', 'SIP URI'), ('tel_url_type', 'TEL URL')
)
SOFTWARE_VERSION_CHOICES = (
    ('', u'指定なし'), ('1.0', 'HDX 1.0'), ('2.0', 'HDX 2.0'),
    ('2.5', u'HDX 2.5以降'), ('8.7.0', u'VSX 8.7以前'),
    ('8.7.1', u'VSX 8.7.1以降'), ('8.0.2', u'PVX 8.0.2以前'),
    ('8.0.4', u'PVX 8.0.4以降')
)
TYPE_CHOICES = (('isdn', 'ISDN/PSTN'), ('h323', 'H.323'), ('sip', 'SIP'))
VIDEO_PROTOCOL_CHOICES = (
    ('auto', u'自動'), ('h261', 'H.261'), ('h263', 'H.263'), ('h264', 'H.264')
)

FORMAT_CHOICES = (('csv', 'csv'),)


class EditForm(forms.Form):
    display_name = forms.CharField(
       max_length=26, required=True,
       widget=forms.TextInput(attrs={'size': 26}))
    direction = forms.ChoiceField(choices=DIRECTION_CHOICES, required=True)
    type = forms.ChoiceField(choices=TYPE_CHOICES, required=True)
    bitrate = forms.TypedChoiceField(
        choices=BITRATE_CHOICES, coerce=int, required=False)
    video_protocol = forms.ChoiceField(
        choices=VIDEO_PROTOCOL_CHOICES, required=True)
    ip_address1 = forms.CharField(
        max_length=3, required=True,
        validators=[
            RegexValidator(regex='^[0-9]+$',
                           message=u'半角数字のみ使用可能です。')],
        widget=forms.TextInput(attrs={'size': 3}))
    ip_address2 = forms.CharField(
        max_length=3, required=True,
        validators=[
            RegexValidator(regex='^[0-9]+$',
                           message=u'半角数字のみ使用可能です。')],
        widget=forms.TextInput(attrs={'size': 3}))
    ip_address3 = forms.CharField(
        max_length=3, required=True,
        validators=[
            RegexValidator(regex='^[0-9]+$',
                           message=u'半角数字のみ使用可能です。')],
        widget=forms.TextInput(attrs={'size': 3}))
    ip_address4 = forms.CharField(
        max_length=3, required=True,
        validators=[
            RegexValidator(regex='^[0-9]+$',
                           message=u'半角数字のみ使用可能です。')],
        widget=forms.TextInput(attrs={'size': 3}))
    phone1 = forms.CharField(
        max_length=32, required=False,
        validators=[
            RegexValidator(regex='^[0-9]+$',
                           message=u'半角数字のみ使用可能です。')],
        widget=forms.TextInput(attrs={'size': 32}))
    alias_name = forms.CharField(
       max_length=16, required=False,
       widget=forms.TextInput(attrs={'size': 16}))
    alias_type = forms.ChoiceField(choices=ALIAS_TYPE_CHOICES, required=False)
    sip_address = forms.CharField(
       max_length=64, required=False,
       widget=forms.TextInput(attrs={'size': 64}))
    sip_address_type = forms.ChoiceField(
        choices=SIP_ADDRESS_TYPE_CHOICES, required=False)
    cascade_role = forms.ChoiceField(
        choices=CASCADE_ROLE_CHOICES, required=False)
    model = forms.ChoiceField(choices=MODEL_CHOICES, required=False)
    software_version = forms.ChoiceField(
        choices=SOFTWARE_VERSION_CHOICES, required=False)
    audio_only_flg = forms.BooleanField(required=False)
    info = forms.CharField(
       max_length=64, required=False,
       widget=forms.TextInput(attrs={'size': 64}))


class DeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['participant_id'] = forms.TypedMultipleChoiceField(
            choices=tuple((x['id'], x['display_name']) for x in
                          Participant.objects.values('id', 'display_name')),
            required=True)


class ImportForm(forms.Form):
    file = forms.FileField()


class ImportRowForm(forms.Form):
    display_name = forms.CharField(max_length=26, required=True)
    direction = forms.ChoiceField(choices=DIRECTION_CHOICES, required=True)
    type = forms.ChoiceField(choices=TYPE_CHOICES, required=True)
    bitrate = forms.TypedChoiceField(
        choices=BITRATE_CHOICES, coerce=int, required=False)
    video_protocol = forms.ChoiceField(
        choices=VIDEO_PROTOCOL_CHOICES, required=True)
    ip_address = forms.CharField(
        max_length=15, required=True,
        validators=[
            RegexValidator(
                regex='^[0-9\.]+$',
                message=u'半角数字と半角ピリオドのみ使用可能です。')])
    phone1 = forms.CharField(
        max_length=32, required=False,
        validators=[
            RegexValidator(
                regex='^[0-9]+$',
                message=u'半角数字のみ使用可能です。')])
    alias_name = forms.CharField(max_length=16, required=False)
    alias_type = forms.ChoiceField(choices=ALIAS_TYPE_CHOICES, required=False)
    sip_address = forms.CharField(max_length=64, required=False)
    sip_address_type = forms.ChoiceField(
        choices=SIP_ADDRESS_TYPE_CHOICES, required=False)
    cascade_role = forms.ChoiceField(
        choices=CASCADE_ROLE_CHOICES, required=False)
    model = forms.ChoiceField(choices=MODEL_CHOICES, required=False)
    software_version = forms.ChoiceField(
        choices=SOFTWARE_VERSION_CHOICES, required=False)
    audio_only_flg = forms.BooleanField(required=False)
    info = forms.CharField(max_length=64, required=False)


class ListAPIForm(forms.Form):
    apiKey = forms.CharField(
        max_length=40, required=True,
        validators=[
            RegexValidator(regex='^{}$'.format(settings.API_KEY),
                           message=u'不正なキーです。')],
       widget=forms.TextInput(attrs={'size': 40}))
    format = forms.ChoiceField(FORMAT_CHOICES, required=False)
