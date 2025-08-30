# Amazon Price Scraper

A simple web scraper built with **Python** using **BeautifulSoup** and **requests** to extract product titles and prices from an Amazon product page. The data is collected and stored in a **CSV** file, allowing for easy tracking of product price changes over time.

## Features

* Scrapes product title and price from an Amazon product page.
* Stores scraped data (title, price, and date) in a CSV file.
* Runs automatically once a day using a continuous loop.

## Prerequisites

Before running the script, ensure you have the required libraries installed:

* `beautifulsoup4`
* `requests`

Install dependencies using pip:

```bash
pip install beautifulsoup4 requests
```

## Usage

1. Clone or download the repository.
2. Replace the `URL` variable with the desired Amazon product URL you want to scrape.
3. Run the script. It will scrape data daily and append the results to `Amazon_Scraper_Dataset.csv`.

```bash
python scraper.py
```

The script will continuously run, collecting data once every 24 hours.

## Disclaimer

Please ensure that scraping Amazon (or any website) complies with their **robots.txt** or **terms of service**. Use responsibly to avoid any legal issues or blocking.

---
