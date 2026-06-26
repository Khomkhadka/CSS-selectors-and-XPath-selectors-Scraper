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
├── requirements.txt
├── README.md   
├── jobs.json
└── jobs.csv

---

## Installation

Clone the repository
git clone https://github.com/Khomkhadka/CSS-selectors-and-XPath-selectors-Scraper.git

Move into the project directory
cd reed_jobs

Install dependencies
pip install -r requirements.txt

---

## Running the Spider

Export to JSON
scrapy crawl data_analyst -O jobs.json [# For json]

Export to CSV
scrapy crawl data_analyst -O jobs.csv

---

## Output

The spider generates:

- jobs.json
- jobs.csv

Each record contains all extracted job information.

---

## Challenges

During development, several challenges were encountered:

- Duplicate job listings across pages
- Multiple metadata formats
- Mixed Contract Type and Job Type values
- Pagination handling
- Missing salary values

These issues were handled using URL deduplication and metadata parsing logic.

---

## Assignment Requirements

✔ Python (Scrapy)

✔ CSS/XPath Selectors

✔ Multi-page Pagination

✔ Detail Page Crawling

✔ JSON Export

✔ CSV Export

✔ No BeautifulSoup

---

## Workflow
             Start
               │
               ▼
             Visit
         
         https://www.reed.co.uk/jobs/data-analyst-jobs
         
               │
               ▼
         Extract Job URLs
         
               │
               ▼
         Remove Duplicate URLs
         
               │
               ▼
         Visit Job Detail Page
         
               │
               ▼
            Extract
         
         • Detail URL
         • Title
         • Salary
         • Contract Type
         • Job Type
         • Location
         
               │
               ▼
           Save Item
         
               │
               ▼
         Visit Next Pagination
         
               │
               ▼
         Repeat Until Last Pagination
         
               │
               ▼
         Export JSON / CSV
         
               │
               ▼
             Finish         

---

## sample of the scraped data
The data will store like this 
#In .json format
[
{"page_number": 1, "detail_url": "https://www.reed.co.uk/jobs/data-analyst/56770926", "title": "Data Analyst", "salary": "£40,000 - £45,000 per annum", "contract_type": "Permanent", "job_type": "Full-Time", "location": "Gillingham, Kent", "listing_page": "https://www.reed.co.uk/jobs/data-analyst-jobs", "scraped_at": "2026-06-26T23:47:03.591882"},
{"page_number": 1, "detail_url": "https://www.reed.co.uk/jobs/data-analyst/56915591", "title": "Data Analyst", "salary": "£40,000 per annum", "contract_type": "Permanent", "job_type": "Full-Time", "location": "Leeds, West Yorkshire", "listing_page": "https://www.reed.co.uk/jobs/data-analyst-jobs", "scraped_at": "2026-06-26T23:47:04.911303"},
{"page_number": 1, "detail_url": "https://www.reed.co.uk/jobs/data-analyst/56917623", "title": "Data Analyst", "salary": "£50 per hour", "contract_type": "Permanent", "job_type": "Full-Time", "location": "Gloucestershire", "listing_page": "https://www.reed.co.uk/jobs/data-analyst-jobs", "scraped_at": "2026-06-26T23:47:06.091699"},
]
#Data sample u can find in jobs.json

---

## Author

Khom Khadka

Bachelor's in Computer Science

Backend Developer

