# -*- coding: utf-8 -*-
import re
from cms.models import CMSPlugin

import warnings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError

CLASS_NAMES = getattr(
    settings,
    "ALDRYN_STYLE_CLASS_NAMES",
    (
        ('container', _("container")),
        ('content', _("content")),
        ('teaser', _("teaser")),
    )
)

CLASS_NAME_FORMAT = re.compile(r'^\w[\w_-]*$')
TAG_TYPE_FORMAT = re.compile(r'\w[\w\d]*$')


def get_html_tag_types():
    tag_types = getattr(settings, "ALDRYN_STYLE_ALLOWED_TAGS", None)
    if tag_types:
        # Remove anything that doesn't look like an HTML tag
        for tag in tag_types:
            tag = tag.strip()
            if not TAG_TYPE_FORMAT.match(tag):
                warnings.warn(_(u'ALDRYN STYLE: "{}" was omitted from '
                                u'ALDRYN_STYLE_ALLOWED_TAGS as it does '
                                u'not look like a valid HTML tag.').format(tag))
                tag_types.remove(tag)

    # Could be that it was initially empty, or, none of the supplied entries
    # looked right, in either of these cases, use the default set as defined
    # in version 1.0.1.
    if tag_types is None:
        tag_types = [
            'div', 'article', 'section', 'span', 'p', 'h1', 'h2', 'h3', 'h4',
        ]

    return tuple([(tag, tag) for tag in tag_types])


class Style(CMSPlugin):
    """
    A CSS Style Plugin
    """
    DIV_TAG = 'div'
    HTML_TAG_TYPES = get_html_tag_types()

    label = models.CharField(_('label'), max_length=128, default="", blank=True,
        help_text=_('Optional label for this style plugin.'))

    cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True)

    class_name = models.CharField(_("class name"), choices=CLASS_NAMES,
        default=CLASS_NAMES[0][0], max_length=50, blank=True)
    id_name = models.CharField(_("id name"), max_length=50, blank=True, default='')

    tag_type = models.CharField(verbose_name=_('tag Type'), max_length=50,
        choices=HTML_TAG_TYPES, default=DIV_TAG)

    padding_left = models.SmallIntegerField(_("padding left"), blank=True, null=True)
    padding_right = models.SmallIntegerField(_("padding right"), blank=True, null=True)
    padding_top = models.SmallIntegerField(_("padding top"), blank=True, null=True)
    padding_bottom = models.SmallIntegerField(_("padding bottom"), blank=True, null=True)

    margin_left = models.SmallIntegerField(_("margin left"), blank=True, null=True)
    margin_right = models.SmallIntegerField(_("margin right"), blank=True, null=True)
    margin_top = models.SmallIntegerField(_("margin top"), blank=True, null=True)
    margin_bottom = models.SmallIntegerField(_("margin bottom"), blank=True, null=True)

    additional_class_names = models.TextField(
        verbose_name=_('additional classes'),
        blank=True,
        help_text=_('Comma separated list of additional classes to apply to tag_type')
    )

    def __unicode__(self):
        display = self.get_class_name_display() or self.tag_type or u''
        if self.additional_class_names:
            display = u'{0} ({1})'.format(display, self.additional_class_names)
        if self.label:
            display = u'“{0}”: {1}'.format(self.label, display)
        return u"%s" % display

    def inline_style(self):
        style = ""
        if self.padding_left:
            style += "padding-left: %dpx; " % self.padding_left
        if self.padding_right:
            style += "padding-right: %dpx; " % self.padding_right
        if self.padding_bottom:
            style += "padding-bottom: %dpx; " % self.padding_right
        if self.padding_top:
            style += "padding-top: %dpx; " % self.padding_top
        if self.margin_left:
            style += "margin-left: %dpx; " % self.margin_left
        if self.margin_right:
            style += "margin-right: %dpx; " % self.margin_right
        if self.margin_top:
            style += "margin-top: %dpx; " % self.margin_top
        if self.margin_bottom:
            style += "margin-bottom: %dpx; " % self.margin_bottom
        return style

    def clean(self):
        if self.additional_class_names:
            additional_class_names = list(
                html_class.strip() for html_class in self.additional_class_names.split(','))
            for class_name in additional_class_names:
                class_name = class_name.strip()
                if not CLASS_NAME_FORMAT.match(class_name):
                    raise ValidationError(u'"%s" is not a proper css class name.' % (class_name, ))
            self.additional_class_names = u", ".join(set(additional_class_names))

    @property
    def get_additional_class_names(self):
        if self.additional_class_names:
            # Removes any extra spaces
            return ' '.join((html_class.strip() for html_class in self.additional_class_names.split(',')))
        return ''
