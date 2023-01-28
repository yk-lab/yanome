from django.db import models
from django.utils.translation import gettext_lazy as _

from lib.models import BaseModel


class Type(models.TextChoices):
    POPUP = 'POPUP', _('ポップアップ')


class Config(BaseModel):
    type = models.CharField(
        choices=Type.choices,
        max_length=16,
        verbose_name=_('種別'),
    )

    memo = models.TextField(
        blank=True,
        default='',
        null=True,
        verbose_name=_('メモ')
    )

    class Meta:
        verbose_name = _('設定')
        verbose_name_plural = _('設定')

    def __str__(self):
        return self.memo or ' - '

    # def get_absolute_url(self):
    #     return reverse('config_detail', kwargs={'pk': self.pk})
