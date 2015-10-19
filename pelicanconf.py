#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hana Lee'
SITENAME = u'Hana Lee'
#SITESUBTITLE = u''
SITEURL = u'http://hanalee.info'

PATH = u'content/'

TIMEZONE = u'America/Chicago'

DEFAULT_LANG = u'en'

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','tables']
THEME = "./built-texts"

DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL='{category}/{slug}.html'
ARTICLE_SAVE_AS='{category}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS =  (('', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/lee_hn'),
          ('github', 'http://github.com/hnlee'),
          ('linkedin', 'http://www.linkedin.com/in/hanalee07'),
          ('google scholar', 'http://scholar.google.com/citations?hl=en&user=dOVsa18AAAAJ'),)
EMAIL = 'hanalee07@gmail.com'
GITHUB_URL = 'http://github.com/hnlee/'

# Colophon
COLOPHON = True
COLOPHON_TITLE = 'Navigation'
COLOPHON_CONTENT = ""

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
