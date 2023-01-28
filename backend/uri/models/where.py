from django.db import models
from django.utils.translation import gettext_lazy as _

from lib.models import BaseModel

from .config import Config


class Where(BaseModel):
    config = models.ForeignKey[Config](
        'Config',
        models.CASCADE,
    )

    uri = models.CharField(
        max_length=2048,
        blank=True,
        null=True,
        verbose_name=_('URI'),
    )

    protocol = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name=_('プロトコル'),
    )

    hostname = models.CharField(
        max_length=512,
        blank=True,
        null=True,
        verbose_name=_('ホスト名'),
    )

    pathname = models.CharField(
        max_length=2048,
        blank=True,
        null=True,
        verbose_name=_('パス名'),
    )

    memo = models.TextField(
        blank=True,
        default='',
        null=True,
        verbose_name=_('メモ'),
    )

    class Meta:
        verbose_name = _('条件式')
        verbose_name_plural = _('条件式')

    def __str__(self):
        return self.memo or ' - '

    # def get_absolute_url(self):
    #     return reverse('where_detail', kwargs={'pk': self.pk})
