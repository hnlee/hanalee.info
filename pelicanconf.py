#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hana Lee'
SITENAME = u'H.N. Lee'
SITEURL = u'http://hanalee.info'

TIMEZONE = u'America/Chicago'

DEFAULT_LANG = u'en'
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','tables']
THEME = "./built-texts"

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
