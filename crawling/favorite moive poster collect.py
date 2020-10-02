from bs4 import BeautifulSoup
from selenium import webdriver
import time

import dload

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=eternal%20sunshine")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기
req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select("#imgList > div > a > img")

i = 1
for thumbnail in thumbnails[:20]:
    src = thumbnail["src"]
    dload.save(src, "movies/{}.jpg".format(i))
    i += 1


driver.quit()