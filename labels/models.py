from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField


class Brand(models.Model):
    name = models.CharField(_('name'), max_length=200)
    background = ColorField(blank=True)

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')
        ordering = ['name']

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(_('name'), max_length=200)
    brand = models.ForeignKey(
        Brand, verbose_name=_('brand'), on_delete=models.PROTECT, related_name='labels', db_index=True, null=True, blank=True,
    )
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')
        ordering = ['name']

    def __str__(self):
        return self.name
