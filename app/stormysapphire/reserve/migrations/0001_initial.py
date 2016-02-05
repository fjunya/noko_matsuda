# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import reserve.models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tms_conferenceId', models.CharField(max_length=30, blank=True)),
                ('mcu_conferenceName', models.CharField(max_length=30, blank=True)),
                ('mcu_conferenceNo', models.CharField(max_length=30, blank=True)),
                ('userName', models.CharField(max_length=50, blank=True)),
                ('department', models.CharField(max_length=50, blank=True)),
                ('mail', models.EmailField(max_length=254, blank=True)),
                ('tel', models.CharField(max_length=50, blank=True)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('title', models.CharField(max_length=100)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('bandwidth', models.CharField(max_length=20)),
                ('videoQuality', models.CharField(max_length=50, blank=True)),
                ('h239', models.CharField(max_length=10, blank=True)),
                ('encrypted', models.CharField(max_length=10)),
                ('pin', models.IntegerField(null=True, blank=True)),
                ('controlPassword', models.CharField(max_length=50, blank=True)),
                ('conferencePassword', models.IntegerField(default=-1)),
                ('chairPassword', models.CharField(max_length=50, blank=True)),
                ('recording', models.BooleanField()),
                ('isWebEx', models.BooleanField()),
                ('mailForWebEx', models.CharField(max_length=500, blank=True)),
                ('layout_mode', models.CharField(max_length=50)),
                ('presenter', models.IntegerField(null=True, blank=True)),
                ('layout_no', models.IntegerField(null=True, blank=True)),
                ('pane1', models.CharField(max_length=50, blank=True)),
                ('pane2', models.CharField(max_length=50, blank=True)),
                ('pane3', models.CharField(max_length=50, blank=True)),
                ('pane4', models.CharField(max_length=50, blank=True)),
                ('pane5', models.CharField(max_length=50, blank=True)),
                ('pane6', models.CharField(max_length=50, blank=True)),
                ('pane7', models.CharField(max_length=50, blank=True)),
                ('pane8', models.CharField(max_length=50, blank=True)),
                ('pane9', models.CharField(max_length=50, blank=True)),
                ('pane10', models.CharField(max_length=50, blank=True)),
                ('pane11', models.CharField(max_length=50, blank=True)),
                ('pane12', models.CharField(max_length=50, blank=True)),
                ('pane13', models.CharField(max_length=50, blank=True)),
                ('pane14', models.CharField(max_length=50, blank=True)),
                ('pane15', models.CharField(max_length=50, blank=True)),
                ('pane16', models.CharField(max_length=50, blank=True)),
                ('isStarted', models.BooleanField()),
                ('use_resource', models.IntegerField()),
                ('createUser', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('participants', models.ManyToManyField(to='participant.Participant')),
            ],
            options={
                'db_table': 'conference',
            },
        ),
        migrations.CreateModel(
            name='RecurrencePattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'recurrence_pattern',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('slot', models.PositiveSmallIntegerField(default=0, validators=[reserve.models.validate_slot])),
                ('conference', models.ForeignKey(to='reserve.Conference')),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='TmsUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'tms_user',
            },
        ),
        migrations.AddField(
            model_name='conference',
            name='recurrencePattern',
            field=models.ForeignKey(blank=True, to='reserve.RecurrencePattern', null=True),
        ),
        migrations.AddField(
            model_name='conference',
            name='tmsUser',
            field=models.ForeignKey(blank=True, to='reserve.TmsUser', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='resource',
            unique_together=set([('conference', 'date', 'slot')]),
        ),
    ]
