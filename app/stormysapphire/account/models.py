from django.contrib.auth.models import User
from django.db import models


class AccountGroup(models.Model):
    name = models.CharField(max_length=24, default='')
    info = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'account_group'


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    dept = models.CharField(max_length=64, blank=True, null=True)
    tel = models.CharField(max_length=32, blank=True, null=True)
    info = models.CharField(max_length=64, blank=True, null=True)
    date_from = models.DateTimeField(null=True)
    date_to = models.DateTimeField(null=True)
    no_validity = models.NullBooleanField()
    reserve_days = models.PositiveSmallIntegerField(blank=True, null=True)
    no_reserve_days = models.NullBooleanField()
    account_groups = models.ManyToManyField(AccountGroup)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'account'
