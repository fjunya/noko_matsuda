# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(default=b'', max_length=40)),
                ('direction', models.CharField(default=b'', max_length=12)),
                ('type', models.CharField(default=b'', max_length=8)),
                ('bitrate', models.PositiveIntegerField(null=True, blank=True)),
                ('video_protocol', models.CharField(default=b'', max_length=8)),
                ('ip_address', models.CharField(default=b'', max_length=32)),
                ('phone1', models.CharField(max_length=32, null=True, blank=True)),
                ('alias_name', models.CharField(max_length=32, null=True, blank=True)),
                ('alias_type', models.CharField(max_length=8, null=True, blank=True)),
                ('sip_address', models.CharField(max_length=80, null=True, blank=True)),
                ('sip_address_type', models.CharField(max_length=24, null=True, blank=True)),
                ('cascade_role', models.CharField(default=b'', max_length=12)),
                ('model', models.CharField(default=b'', max_length=12)),
                ('software_version', models.CharField(default=b'', max_length=12)),
                ('audio_only_flg', models.NullBooleanField()),
                ('info', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
                'db_table': 'participant',
            },
        ),
        migrations.CreateModel(
            name='ParticipantGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(default=b'', max_length=24)),
                ('info', models.CharField(max_length=128, null=True, blank=True)),
                ('participants', models.ManyToManyField(to='participant.Participant')),
            ],
            options={
                'db_table': 'participant_group',
            },
        ),
    ]
