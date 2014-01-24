# -*- coding: utf-8 -*-
from cmscloud_client import forms

from aldryn_style.utils import CLASS_NAME_FORMAT


class ClassNamesField(forms.CharField):

    def clean(self, value):
        value = super(ClassNamesField, self).clean(value)
        value = filter(bool, map(lambda x: x.strip(), value.split(',')))
        for class_name in value:
            if not CLASS_NAME_FORMAT.match(class_name):
                raise forms.ValidationError(u'%s is not a proper class name.' % (class_name, ))
        return value


class Form(forms.BaseForm):

    class_names = ClassNamesField('Class names', max_length=100)

    def to_settings(self, data, settings):
        settings['ALDRYN_STYLE_CLASS_NAMES'] = data['class_names']
        return settings
