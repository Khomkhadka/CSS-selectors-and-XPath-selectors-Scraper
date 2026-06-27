import scrapy
from datetime import datetime


class DataAnalystSpider(scrapy.Spider):

    name = "data_analyst"
    allowed_domains = ["reed.co.uk"]

    base_url = "https://www.reed.co.uk/jobs/data-analyst-jobs"
    start_urls = [base_url]

    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "AUTOTHROTTLE_ENABLED": True,
        "ROBOTSTXT_OBEY": False,
        "DUPEFILTER_DEBUG": True,
        "FEEDS": {
            "jobs.json": {
                "format": "json",
                "encoding": "utf8",
                "overwrite": True
            },
            "jobs.csv": {
                "format": "csv",
                "encoding": "utf8",
                "overwrite": True,
            }
        }
    }

    visited_urls = set()

    def parse(self, response):

        page = response.meta.get("page", 1)

        self.logger.info(f"Scraping page {page}: {response.url}")

        job_links = response.css(
            'a[data-qa="job-card-title"]::attr(href)'
        ).getall()

        self.logger.info(f"Jobs found: {len(job_links)}")

        # -----------------------------
        # STOP CONDITIONS (CRITICAL)
        # -----------------------------

        if response.status != 200:
            self.logger.info("Non-200 response → stopping spider")
            return

        if not job_links:
            self.logger.info("No jobs found → stopping spider")
            return

        if len(job_links) < 5:
            self.logger.info("Last page detected (few jobs) → stopping spider")
            return

        # -----------------------------
        # EXTRACT JOBS
        # -----------------------------

        for link in job_links:

            job_url = response.urljoin(link).split("?")[0]

            if job_url in self.visited_urls:
                continue

            self.visited_urls.add(job_url)

            yield scrapy.Request(
                url=job_url,
                callback=self.parse_job,
                meta={
                    "page": page,
                    "listing_page": response.url
                }
            )

        # -----------------------------
        # PAGINATION
        # -----------------------------

        next_link = response.css("a.page-link.next::attr(href)").get()

        if next_link:

            yield scrapy.Request(
                url=response.urljoin(next_link),
                callback=self.parse,
                meta={"page": page + 1}
            )

        else:
            self.logger.info("No next page → spider finished")
            return

    def parse_job(self, response):

        page = response.meta.get("page")
        listing_page = response.meta.get("listing_page")

        def clean(value):
            return " ".join(value.split()) if value else None

        # -----------------------------
        # Direct Salary Extraction
        # -----------------------------
        salary = clean(
            response.css(
                'li[data-qa="job-metadata-salary"]::text'
            ).get()
        )

        if not salary:
            salary = clean(
                " ".join(
                    response.css(
                        'li[data-qa="job-metadata-salary"] *::text'
                    ).getall()
                )
            )

        # -----------------------------
        # Direct Location Extraction
        # -----------------------------
        location = clean(
            response.css(
                'li[data-qa="job-metadata-location"]::text'
            ).get()
        )

        if not location:
            location = clean(
                " ".join(
                    response.css(
                        'li[data-qa="job-metadata-location"] *::text'
                    ).getall()
                )
            )

        # Keep metadata for contract/job type only
        metadata = response.css(
            '[data-qa="job-metadata"] li::text'
        ).getall()

        metadata = [clean(x) for x in metadata if clean(x)]

        contract_type = None
        job_type = None

        for item in metadata:

            text = item.lower()

            if "," in item:
                parts = [p.strip() for p in item.split(",")]

                for part in parts:
                    p = part.lower()

                    if p in [
                        "permanent",
                        "contract",
                        "temporary",
                        "fixed-term contract",
                        "internship"
                    ]:
                        contract_type = part.title()

                    elif p in [
                        "full-time",
                        "part-time",
                        "full time",
                        "part time"
                    ]:
                        job_type = part.title()

                continue

            if text in [
                "permanent",
                "contract",
                "temporary",
                "fixed-term contract",
                "internship"
            ]:
                contract_type = item.title()
                continue

            if text in [
                "full-time",
                "part-time",
                "full time",
                "part time"
            ]:
                job_type = item.title()
                continue

        yield {
            "page_number": page,
            "detail_url": response.url,
            "title": clean(response.css("h1::text").get()),
            "salary": salary,
            "contract_type": contract_type,
            "job_type": job_type,
            "location": location,
            "listing_page": listing_page,
            "scraped_at": datetime.now().isoformat()
        }