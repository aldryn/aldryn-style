# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


from aldryn_style.models import StylePlugin


class ClassNameWidget(forms.MultiWidget):

    def __init__(self):
        self.options = getattr(settings, 'STYLE_CLASS_NAMES', [])
        choices = [(x, x) for x in self.options]
        choices.append(('', _('Enter manually')))
        widgets = [forms.Select(choices=choices), forms.TextInput()]
        super(ClassNameWidget, self).__init__(widgets)

    class Media:
        js = ['aldryn_style/js/class_name_widget.js']

    def decompress(self, value):
        select_visible = value in self.options
        return (value, '') if select_visible else ('', value)

    def value_from_datadict(self, *args, **kwargs):
        value = super(ClassNameWidget, self).value_from_datadict(*args, **kwargs)
        (select_value, text_input_value) = value
        return select_value or text_input_value

    def format_output(self, rendered_widgets):
        return mark_safe(' '.join(rendered_widgets))


class StyleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StyleForm, self).__init__(*args, **kwargs)
        self.fields['class_name'].widget = ClassNameWidget()

    class Meta:
        model = StylePlugin
