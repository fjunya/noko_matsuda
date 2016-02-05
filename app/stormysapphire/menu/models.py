from django.db import models

from django.contrib.auth.models import User


class Information(models.Model):
    MENU_TYPE = 1

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField(blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'information'
