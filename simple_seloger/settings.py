# -*- coding: utf-8 -*-

# Scrapy settings for simple_seloger project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.exporters import JsonLinesItemExporter

BOT_NAME = 'simple_seloger'

SPIDER_MODULES = ['simple_seloger.spiders']

NEWSPIDER_MODULE = 'simple_seloger.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit /537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Crawlera proxy settings
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_crawlera.CrawleraMiddleware': 300,
# }

# CRAWLERA_APIKEY = '6520342f00ec43ba974c6012955fa9cf'

# CRAWLERA_ENABLED = False

# AUTOTHROTTLE_ENABLED = False

# Correctly show accents in JSON output
FEED_EXPORT_ENCODING = 'utf-8'

# Specifies exported fields and order
FEED_EXPORT_FIELDS = ["plateforme", "type_bien", "prix", "surface", "ville", "les_plus",
                      "general", "interieur", "exterieur", "diag_perf_energie", "indice_gaz"]

DEFAULT_REQUEST_HEADERS = {
    'Referer': 'http://www.seloger.com'
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'simple_seloger.pipelines.MongoDbPipeline': 300,
}

MONGO_URI = 'mongodb://heroku_s69f85gw:16inpkg7t0g007tgosilqqme6@ds019882.mlab.com:19882/heroku_s69f85gw'

MONGO_DB = 'heroku_s69f85gw'

#DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

#DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

#REDIRECT_ENABLED = False

##############################################

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'simple_seloger.middlewares.DemoProjectSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'simple_seloger.middlewares.DemoProjectDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
