#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

# inherits sitedev configuration
from sitedev import *

RELATIVE_URLS = False
GOOGLE_ANALYTICS = 'UA-96374238-1'
FEED_EMAIL = 'https://feedburner.google.com/fb/a/mailverify?uri=voraklfeed/atom&amp;loc=en_US'
FEED_DOMAIN = 'http://feeds.feedburner.com'