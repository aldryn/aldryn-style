# -*- coding: utf-8 -*-
from cmscloud_client import forms

import re


class ClassNamesField(forms.CharField):

    CLASS_NAME_RE = re.compile(r'^\w[\w-_]*$')

    def clean(self, value):
        value = super(ClassNamesField, self).clean(value)
        value = filter(bool, map(lambda x: x.strip(), value.split(',')))
        for class_name in value:
            if not self.CLASS_NAME_RE.match(class_name):
                raise forms.ValidationError(u'%s is not a proper class name.' % (class_name, ))
        return value


class Form(forms.BaseForm):

    class_names = ClassNamesField('Class names')

    def to_settings(self, data, settings):
        settings['STYLE_CLASS_NAMES'] = data['class_names']
        return settings
