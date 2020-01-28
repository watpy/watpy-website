#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'WatPy Members'
SITENAME = 'WatPy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/watpy'),
          ('Meetup', 'https://www.meetup.com/watpymeetup/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Buruma-related configuration.
# More settings: https://buruma.ivanhercaz.com/settings
THEME = "themes/buruma"
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", ]
CATS_NOT_DROPDOWN = True
WELCOME_HEADING = "WatPy is the Waterloo region Python users group."
LICENSE = True
LICENSE_NOTICE = "Licensed under the Creative Commons Attribution-ShareAlike 4.0 International License"
