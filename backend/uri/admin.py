from django.contrib import admin

from .models import Config, Where


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass


@admin.register(Where)
class WhereAdmin(admin.ModelAdmin):
    pass
