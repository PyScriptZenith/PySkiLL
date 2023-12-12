import datetime

from django.db import models

from users.models import User




NULLABLE = {"null": True, "blank": True}
class Dispatch(models.Model):
    mail_to_send = models.EmailField(verbose_name='почта для рассылки')

    def __str__(self):
        return f'{self.mail_to_send} '
    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
