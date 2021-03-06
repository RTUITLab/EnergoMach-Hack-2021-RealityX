from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class Subsidy(models.Model):
    kbk = models.CharField('KBK', max_length=250, default='none')
    purpose = models.CharField('Purpose', max_length=250, default='none')
    info = models.JSONField('info', null=True, blank=True)

    class Meta:
        verbose_name = 'Subsidy'
        verbose_name_plural = 'Subsidies'

    def __str__(self):
        return f'({self.kbk}) {self.purpose}'


class User(AbstractUser):
    company = models.JSONField('Company', null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'({self.id}) {self.username}'
