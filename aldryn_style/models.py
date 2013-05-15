# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


def get_class_choices():
    return [(x, x) for x in getattr(settings, 'STYLE_CLASS_NAMES', [''])]


class StylePlugin(CMSPlugin):

    class_name = models.CharField(_('Class name'), choices=get_class_choices(), max_length=50)

    def __unicode__(self):
        return self.class_name
