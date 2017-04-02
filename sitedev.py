#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### Basic configuration
########################

AUTHOR = u'Oleksii Tsvietnov'
SITENAME = u"Engineer's notes"
SITEURL = 'http://vorakl.name'
SITEDESC = u'A technical blog of Oleksii Tsvietnov about Software Engineering'
PATH = 'content' # the location of all content
ARTICLE_PATHS = ['articles'] # a place for articles under the content location
CONTACT_PAGE = 'about'
TIMEZONE = 'Europe/Berlin'
THEME = "/home/vorakl/repos/my/bitbucket/vorakl.github.io/theme"
DEFAULT_LANG = u'en'
RELATIVE_URLS = True  # disable in public version
DEFAULT_PAGINATION = 2 
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
PLUGINS = ['minify']

DELETE_OUTPUT_DIRECTORY = True  # build an output dir from scratch every time
OUTPUT_RETENTION = [".git", "CNAME", "README.md"] # but these dirs and files should be kept


### Interface configuration
############################

#MENUITEMS = [("Github", "https://github.com/vorakl"), ("LinkedIn", "https://linkedin.com/in/vorakl/")]
DISPLAY_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_SIDEBAR = True
DISPLAY_ARCHIVES_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_AUTHORS_ON_SIDEBAR = False # It's turned off because I'm the only one author on this site
DISPLAY_SUBSCRIBES_ON_SIDEBAR = True
DISPLAY_SITE_ON_SIDEBAR = True

DISPLAY_AUTHOR = False # Add an author in a article's metadata


### Feed's specification 
#########################

FEED_EMAIL = None # disable in development version
FEED_DOMAIN = '' # and create all feed under the local domain for testing purpose
FEED_MAX_ITEMS = 15
FEED_ALL_ATOM = 'voraklfeed/atom'
FEED_ALL_RSS = None # Here is used the only one feed on Google's feedburner. All other feeds are disabled
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None


### Static files (non templates)
#################################

STATIC_PATHS = [
    'articles', 
    'images', 
    'files', 
    'static/robots.txt', 
    'static/favicon.ico', 
    'static/google747986e3861ca881.html'
    ]
# and sprecial output paths for them
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/google747986e3861ca881.html': {'path': 'google747986e3861ca881.html'}
    }


### Templates for html pages
#############################

# blog posts related pages

# If there is a 'Save_as' metadata (like in 404.html), then a page will be rendered anyway
ARTICLE_SAVE_AS = '{category}/{slug}/index.html' # activates rendering each article
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}/index.html'
ARTICLE_LANG_URL = '{category}/{slug}-{lang}/'
DRAFT_SAVE_AS = 'drafts/{category}/{slug}/index.html' # activates rendering each article's draft
DRAFT_URL = 'drafts/{category}/{slug}/'
DRAFT_LANG_SAVE_AS = 'drafts/{category}/{slug}-{lang}/index.html'
DRAFT_LANG_URL = 'drafts/{category}/{slug}-{lang}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'  # activates rendering each page.
PAGE_URL = 'pages/{slug}/'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}/index.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html' # activates rendering each category
CATEGORY_URL = 'category/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html' # activates rendering each tag
TAG_URL = 'tag/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html' # activates rendering each author
AUTHOR_URL = 'author/{slug}/'

# site related pages

# a list of templates for rendering blog posts. Not all of them, just an index and groups of entities (tags, categories, ...)
# other templates for blog posts rendering (for a tag, a category, ...) are activated by *_SAVE_AS variables below
DIRECT_TEMPLATES = ['index', 'categories', 'tags', 'authors', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['index']

INDEX_SAVE_AS = 'index.html'
AUTHORS_SAVE_AS = 'author/index.html'  # defines where to save an authors page, it's activated by DIRECT_TEMPLATES 
AUTHORS_URL = 'author/'
ARCHIVES_SAVE_AS = 'archives/index.html' # defines where to save an archives page, it's activated by DIRECT_TEMPLATES 
ARCHIVES_URL = 'archives/'
TAGS_SAVE_AS = 'tag/index.html' # defines where to save a tags page, it's activated by DIRECT_TEMPLATES
TAGS_URL = 'tag/'
CATEGORIES_URL = 'category/' # defines where to save a categories page, it's activated by DIRECT_TEMPLATES
CATEGORIES_SAVE_AS = 'category/index.html'

YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html' # activates rendering an archive page per year/month/day
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''

# additional pages

# a hash array with an extra list of 'templates+output_filename' for rendering besides of blog posts
# The output filename is needed because they don't have *_SAVE_AS variables
TEMPLATE_PAGES = {'sitemap.html': 'sitemap.xml'} 

