============
Aldryn Style
============

A Plugin for django CMS to add CSS classes to other plugins.

------------
Installation
------------

This plugin requires `django CMS` 2.4 or higher to be properly installed.

* Create a `virtualenv` and run ``pip install aldryn-style``
* Add ``'aldryn_style'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate aldryn_style``.

-----
Usage
-----

You can define styles in your settings.py:

```
gettext = lambda s: s
ALDRYN_STYLE_CLASS_NAMES = (
    ('info', gettext('info')),
    ('new', gettext('new')),
    ('hint', gettext('hint')),
)
```

After that you can place other plugins inside this style plugin.
It will create a div with a class that was prior selected around this plugin.

------------
Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/aldryn-style/
