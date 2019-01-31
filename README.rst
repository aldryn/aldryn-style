**Deprecated**

This project has been succeeded by `djangocms-style <https://github.com/divio/djangocms-style/>`_ , and is no longer supported.

Divio will undertake no further development or maintenance of this project. If you are interested in  taking responsibility for this project as its maintainer, please contact us via www.divio.com.


============
Aldryn Style
============

Aldryn Style provides a plugin that wraps other plugins in CSS styling, by
placing a class name on a containing element.

------------
Installation
------------

This plugin requires `django CMS` 2.4 or higher to be properly installed.

* Within your ``virtualenv`` run ``pip install aldryn-style``
* Add ``'aldryn_style'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate aldryn_style``.

-----
Usage
-----

You can define styles and tag-types in your settings.py::

    # define this lambda if it isn't already defined in your settings...
    _ = lambda s: s

    ALDRYN_STYLE_CLASS_NAMES = (
        ('info', _('info')),
        ('new', _('new')),
        ('hint', _('hint')),
    )

    ALDRYN_STYLE_ALLOWED_TAGS = [
        'div', 'p', 'span', 'article', 'section', 'header', 'footer',
    ]

By default, if ``ALDRYN_STYLE_ALLOWED_TAGS`` is not supplied, or contains an
empty list, then it will default to the following list for backwards
compatibility with previous versions::

    ALDRYN_STYLE_ALLOWED_TAGS = [
        'div', 'article', 'section', 'p', 'span',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'header', 'footer',
    ]

NOTICE::

    All tags included in this list should be "paired tags" that require a
    closing tag. It does not make sense to attempt to use 'button', 'input',
    'img', or other self-closing tag in this setting.

    Also, the developer is advised to choose the tag-types wisely to avoid HTML
    validation issues and/or unintentional security vulnerabilities. For
    example, the 'script' tag should never be allowed in
    ``ALDRYN_STYLE_ALLOWED_TAGS`` (though, we do not prevent this). If you have
    an application where you find yourself wishing to do this, please see
    djangocms-snippet or aldryn-snippet as an alternative, but note these
    projects also come with appropriate security warnings.

After that you can place any number of other plugins inside this style plugin.
It will create a div (or other tag-type) with a class that was prior selected
around the contained plugins.

------------
Translations
------------

If you want to help translate the plugin please do it on Transifex:

https://www.transifex.com/projects/p/django-cms/resource/aldryn-style/
