# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.CharField(max_length=64, null=True, blank=True)),
                ('tel', models.CharField(max_length=32, null=True, blank=True)),
                ('info', models.CharField(max_length=64, null=True, blank=True)),
                ('date_from', models.DateTimeField(null=True)),
                ('date_to', models.DateTimeField(null=True)),
                ('no_validity', models.NullBooleanField()),
                ('reserve_days', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('no_reserve_days', models.NullBooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='AccountGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=24)),
                ('info', models.CharField(max_length=64, null=True, blank=True)),
            ],
            options={
                'db_table': 'account_group',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='account_groups',
            field=models.ManyToManyField(to='account.AccountGroup'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
