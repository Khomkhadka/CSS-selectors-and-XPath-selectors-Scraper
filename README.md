# Reed Data Analyst Job Scraper

## Overview

This project is developed using the Python Scrapy framework to scrape Data Analyst job listings from Reed.co.uk.

The spider starts from the Data Analyst jobs listing page and automatically visits every pagination. For each job posting, it follows the detail page and extracts the required information.

The scraper uses CSS selectors and XPath selectors only.

---

## Objective

The objective of this project is to scrape job information from

https://www.reed.co.uk/jobs/data-analyst-jobs

including all available paginated job listings.

---

## Technologies Used

- Python 3.13
- Scrapy 2.16
- CSS Selectors
- XPath
- JSON
- CSV

---

## Extracted Fields

The scraper collects the following information from every job detail page.

| Field         | Description |
|---------------|-------------|
| Detail URL    | Job detail page URL |
| Title         | Job title |
| Salary        | Salary information |
| Contract Type | Permanent / Contract / Temporary |
| Job Type      | Full-time / Part-time |
| Location      | Job location |
| Pagination    | Pagination number from which the job was discovered |
| Scraped At    | Date and time when the record was scraped |

---

## Features

- Scrapy framework implementation
- CSS and XPath selectors
- Handles multi-page pagination
- Removes duplicate job URLs
- Visits each job detail page
- Supports JSON and CSV export
- Logs crawling progress
- Human-readable project structure

---

## Project Structure
reed_job/
│
├── reed_job/
│ ├── spiders/
│ │ └── data_analyst.py
│ ├── settings.py
│ ├── pipelines.py
│ └── items.py
│
├── scrapy.cfg
├── README.md   
├── jobs.json
└── jobs.csv

---

## Installation

Clone the repository
git clone <repository-url>
