# -*- encoding: utf-8 -*-
import datetime
import logging

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from japan_holiday import JapanHoliday

logger = logging.getLogger('common')


class Command(BaseCommand):
    help = u'Google Calendar API から指定の年の日本の祝日一覧を取得する'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int)

    def handle(self, *args, **options):
        holidays = JapanHoliday(settings.GOOGLE_API_KEY
                                ).get_holiday_calender(options['year'])
        for x in holidays:
            print u'\'{:%Y-%m-%d}\': \'{}\''.format(x.date, x.holiday_name)
