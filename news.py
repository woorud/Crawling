from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook
# import datetime


driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select("#main_pack > div.news.mynews.section._prs_nws > ul > li")

wb = Workbook()
ws = wb.active
ws.title = "Articles"
ws.append(["Title", "Url", "Company", "Thumbnails"])

for article in articles:
    title = article.select_one("dl > dt > a").text
    news_url = article.select_one("dl > dt > a")["href"]
    broadcasting_station = article.select_one("span._sp_each_source").text.split(" ")[0].replace("언론사", "")
    # print(title, news_url, broadcasting_station)
    thumbnail = article.select_one("div > a > img")["src"]

    ws.append([title, news_url, broadcasting_station, thumbnail])

driver.quit()
wb.save(filename="Article.xlsx")

