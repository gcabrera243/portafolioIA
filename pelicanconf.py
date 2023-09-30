AUTHOR = 'Gaston Cabrera'
SITENAME = 'Portafolio IA'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'ES'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'attila-1.6'


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


MENUITEMS = (('Home', '/'),
             ('UT1', '/category/ut1.html'),
             ('UT2', '/category/ut2.html'),
             ('UT3', '/category/ut3.html'),
             ('UT4', '/category/ut4.html'),
             ('UT5', '/category/ut5.html'),
             ('UT6', '/category/ut6.html'),
             ('UT7', '/category/ut7.html'))
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True