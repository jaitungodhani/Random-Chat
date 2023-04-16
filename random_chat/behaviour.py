from django.db import models
from django.utils.translation import gettext_lazy as _

class DateMixin(models.Model):
    date_created = models.DateTimeField(
        verbose_name=_("Date Created"),
        auto_now_add=True
    )
    date_updated = models.DateTimeField(
        verbose_name=_("Date updated"),
        auto_now=True
    )

    class Meta:
        abstract = True