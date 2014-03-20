#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from hashlib import md5

AUTHOR = u'Piyush'
AUTHOR_EMAIL = u'piyush.devel@gmail.com'
SITENAME = u'Piyush Bansal'
TAGLINE = u'One of the nodes in the interwebs.'
SITEURL = ''

PROFILE_IMG_URL = u'http://www.gravatar.com/avatar/%s?s=500'%md5(AUTHOR_EMAIL).hexdigest()

TIMEZONE = u'Asia/Calcutta'
DEFAULT_DATE_FORMAT = u'%b %d, %Y'

DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = u'Misc.'

# Blogroll
LINKS = ()
SOCIAL = (
    ('GitHub', 'https://github.com/piyushbansal'),
    ('LinkedIn', 'https://www.linkedin.com/in/jamescooke'),
)

MENUITEMS = [('Home', '/'), ('About', '/pages/hello-i-am-piyush.html'),]
DISPLAY_PAGES_ON_MENU = False

TYPOGRIFY = True


THEME = '/home/piyush/droidstrap'
DISQUS_SITENAME = "piyushbansal93"
