#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hana Lee'
SITENAME = u'Lee HN'
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
LINKS =  (('?', '#'),
          ('?', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/lee_hn'),
          ('github', 'http://github.com/hnlee'),
          ('linkedin', 'http://www.linkedin.com/pub/hana-lee/45/7a/409'),
          ('email', 'mailto:hanalee@uchicago.edu'),)

GITHUB_URL = 'http://github.com/hnlee/'

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
