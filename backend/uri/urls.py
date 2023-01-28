from django.urls import path

from .apps import UriConfig
from .views import TopView

app_name = UriConfig.name

urlpatterns = [
    path('', TopView.as_view()),
]
