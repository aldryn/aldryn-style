# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from aldryn_style import models


class StylePlugin(CMSPluginBase):

    render_template = 'aldryn_style/style.html'
    name = _('Style')
    model = models.StylePlugin
    allow_children = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(StylePlugin)
