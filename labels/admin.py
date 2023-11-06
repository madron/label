from django.contrib import admin
from django.utils.translation import gettext as _
from . import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'background',)


@admin.register(models.Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)
