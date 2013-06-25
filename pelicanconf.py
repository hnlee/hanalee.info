#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Hana Lee'
SITENAME = u'Genetic Cartography'
SITESUBTITLE = u'website and blog by Hana Lee'
SITEURL = u'http://hanalee.info'
TIMEZONE = u'America/Chicago'

DEFAULT_LANG = u'en'
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra','tables']
THEME = "./built-texts"

DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/lee_hn'),
          ('github', 'http://github.com/hnlee'),
          ('linkedin', 'http://www.linkedin.com/pub/hana-lee/45/7a/409'),
          ('google scholar', 'http://scholar.google.com/citations?hl=en&user=dOVsa18AAAAJ'),)
EMAIL = 'hanalee@uchicago.edu'
GITHUB_URL = 'http://github.com/hnlee/'

# Colophon
COLOPHON = True
COLOPHON_TITLE = 'About'
COLOPHON_CONTENT = "I am a postdoctoral researcher with Joy Bergelson\'s group in the Department of Ecology and Evolution at the University of Chicago. My research interests focus on using genomics to interrogate the genetic basis of ecologically relevant traits in natural populations and gain a better understanding of evolutionary mechanisms at the molecular level. Currently, I am investigating the effects of host genetic background on endophytic microbial communities found in <em>Arabidopsis thaliana</em>."

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
