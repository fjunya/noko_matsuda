from datetime import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from participant.models import Participant


class RecurrencePattern(models.Model):
    class Meta:
        db_table = 'recurrence_pattern'


class TmsUser(models.Model):
    class Meta:
        db_table = 'tms_user'


class Conference(models.Model):
    tms_conferenceId = models.CharField(max_length=30,blank=True)
    mcu_conferenceName = models.CharField(max_length=30,blank=True)
    mcu_conferenceNo = models.CharField(max_length=30,blank=True)
    userName = models.CharField(max_length=50,blank=True)
    department = models.CharField(max_length=50,blank=True)
    mail = models.EmailField(blank=True)
    tel = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=100,blank=True)
    title = models.CharField(max_length=100,blank=False)
    startTime = models.DateTimeField(blank=False)
    endTime = models.DateTimeField(blank=False)
    bandwidth = models.CharField(max_length=20)
    videoQuality = models.CharField(max_length=50, blank=True)
    h239 = models.CharField(max_length=10, blank=True)
    encrypted = models.CharField(max_length=10)
    pin = models.IntegerField(blank=True,null=True)
    controlPassword = models.CharField(max_length=50,blank=True)
    conferencePassword = models.IntegerField(default=-1)
    chairPassword = models.CharField(max_length=50,blank=True)
    participants = models.ManyToManyField(Participant)
    recording = models.BooleanField()
    isWebEx = models.BooleanField()
    mailForWebEx = models.CharField(max_length=500,blank=True)
    createUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    layout_mode = models.CharField(max_length=50)
    presenter = models.IntegerField(null=True,blank=True)
    layout_no = models.IntegerField(null=True,blank=True)
    pane1 = models.CharField(max_length=50,blank=True)
    pane2 = models.CharField(max_length=50,blank=True)
    pane3 = models.CharField(max_length=50,blank=True)
    pane4 = models.CharField(max_length=50,blank=True)
    pane5 = models.CharField(max_length=50,blank=True)
    pane6 = models.CharField(max_length=50,blank=True)
    pane7 = models.CharField(max_length=50,blank=True)
    pane8 = models.CharField(max_length=50,blank=True)
    pane9 = models.CharField(max_length=50,blank=True)
    pane10 = models.CharField(max_length=50,blank=True)
    pane11 = models.CharField(max_length=50,blank=True)
    pane12 = models.CharField(max_length=50,blank=True)
    pane13 = models.CharField(max_length=50,blank=True)
    pane14 = models.CharField(max_length=50,blank=True)
    pane15 = models.CharField(max_length=50,blank=True)
    pane16 = models.CharField(max_length=50,blank=True)
    recurrencePattern = models.ForeignKey(RecurrencePattern,blank=True,null=True)
    tmsUser = models.ForeignKey(TmsUser,blank=True,null=True)
    isStarted = models.BooleanField()
    use_resource = models.IntegerField()

    class Meta:
        db_table = 'conference'


def validate_slot(value):
    if not (value >= 0 and value <= 144):
         raise ValidationError('Invalid slot')


class Resource(models.Model):
    MAX_RESOURCES = 58

    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    slot = models.PositiveSmallIntegerField(default=0, 
                                            validators=[validate_slot])

    class Meta:
        db_table = 'resource'
        unique_together = (('conference', 'date', 'slot'),)
