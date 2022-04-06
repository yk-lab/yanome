from model_utils.models import TimeStampedModel, UUIDModel


class BaseModel(UUIDModel, TimeStampedModel):
    class Meta:
        abstract = True
