from django.db import models
from django.utils.translation import gettext_lazy as _

from lib.models import BaseModel

from .config import Config


class ComponentType(models.TextChoices):
    TEXT = 'TEXT', _('テキスト')


class Component(BaseModel):
    config = models.ForeignKey[Config](
        'Config',
        models.CASCADE,
    )
    type = models.CharField(
        choices=ComponentType.choices,
        max_length=16,
        verbose_name=_('種別'),
    )
