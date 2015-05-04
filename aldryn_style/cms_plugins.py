from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from aldryn_style.models import Style


class StylePlugin(CMSPluginBase):
    model = Style
    name = _("Style")
    render_template = "aldryn_style/plugin.html"
    allow_children = True

    fieldsets = (
        (None, {
            'fields': ('label', 'class_name', )
        }),
        (_('Advanced Settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'additional_class_names',
                'id_name',
                ('padding_left', 'padding_right', 'padding_top', 'padding_bottom'),
                ('margin_left', 'margin_right', 'margin_top', 'margin_bottom'),
            ),
        }),
    )

plugin_pool.register_plugin(StylePlugin)
