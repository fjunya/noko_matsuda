from django.db import models


class Participant(models.Model):
    display_name = models.CharField(max_length=40, default='')
    direction = models.CharField(max_length=12, default='')
    type = models.CharField(max_length=8, default='')
    bitrate = models.PositiveIntegerField(blank=True, null=True)
    video_protocol = models.CharField(max_length=8, default='')
    ip_address = models.CharField(max_length=32, default='')
    alias_name = models.CharField(max_length=32, blank=True, null=True)
    phone1 = models.CharField(max_length=32, blank=True, null=True)
    alias_name = models.CharField(max_length=32, blank=True, null=True)
    alias_type = models.CharField(max_length=8, blank=True, null=True)
    sip_address = models.CharField(max_length=80, blank=True, null=True)
    sip_address_type = models.CharField(max_length=24, blank=True, null=True)
    cascade_role = models.CharField(max_length=12, default='')
    model = models.CharField(max_length=12, default='')
    software_version = models.CharField(max_length=12, default='')
    audio_only_flg = models.NullBooleanField()
    info = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'participant'


class ParticipantGroup(models.Model):
    group_name = models.CharField(max_length=24, default='')
    info = models.CharField(max_length=128, blank=True, null=True)
    participants = models.ManyToManyField(Participant)

    class Meta:
        db_table = 'participant_group'
