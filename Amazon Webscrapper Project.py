import writer as writer
from bs4 import BeautifulSoup as bp
import requests
import time
import datetime
import smtplib


def _scrape(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup = bp(page.content, 'html.parser')
    te = soup.find(id='productTitle')
    title = te.get_text(strip=True) if te else "Title not found."
    pe = soup.find(class_='a-offscreen')
    price = pe.get_text(strip=True) if pe else "Price not found."
    price = price.strip()[1:]
    title = title.strip()
    import datetime
    today = datetime.date.today()

    import csv
    Header = ['Title','Price','Date']
    Data = [title,price,today]
    # Run this ones to create the csv file and then run the 2nd one to fill it with data.
    #with open('Amazon Scrapper dataset3.csv', 'a+', newline='', encoding='UTF8') as f:
        #writer = csv.writer(f)
        #writer.writerow(Header)
        #writer.writerow(Data)
    with open('Amazon Scrapper dataset4.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(Data)

URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'


# This will run ones a day.
while(True):
    _scrape(URL)
    time.sleep(86400)