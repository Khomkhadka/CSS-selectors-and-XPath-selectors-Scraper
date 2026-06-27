BOT_NAME = "reed_jobs"

SPIDER_MODULES = ["reed_jobs.spiders"]
NEWSPIDER_MODULE = "reed_jobs.spiders"

DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True

CONCURRENT_REQUESTS = 4
CONCURRENT_REQUESTS_PER_DOMAIN = 2

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10

RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = True

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

ITEM_PIPELINES = {
    # "reed_jobs.pipelines.CleanDataPipeline": 100,
    # "reed_jobs.pipelines.ExcelExportPipeline": 200,
}

LOG_LEVEL = "INFO"
FEED_EXPORT_ENCODING = "utf-8"