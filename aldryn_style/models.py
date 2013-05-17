# -*- coding: utf-8 -*-
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from aldryn_style.utils import CLASS_NAME_FORMAT


class StylePlugin(CMSPlugin):

    class_name = models.CharField(_('Class name'), max_length=50, validators=[RegexValidator(CLASS_NAME_FORMAT)])

    def __unicode__(self):
        return self.class_name
