from logging import getLogger

from django.db.models import F, Value
from django.views.generic import TemplateView

from ..models import Config

logger = getLogger(__name__)


class TopView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        logger.info(kwargs)

        context = super().get_context_data(**kwargs)
        target = 'http://www.google.co.jp'
        # context["c"] = Config.objects\
        #     .filter(where__uri__regex=target)
        context["c"] = Config.objects\
            .annotate(target=Value(target))\
            .filter(target__regex=F('where__uri'))
        return context
