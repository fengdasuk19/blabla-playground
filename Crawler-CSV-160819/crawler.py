from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import time

originURLroot = 'http://yenchingacademy.org/list/6/date/2017/p/'

with open('test.txt', 'w') as testfile:
    for iDigit in range(1, 13 + 1):
        # Crawling
        originURL = originURLroot + str(iDigit)
        webDataRaw = requests.get(originURL)
        webData = webDataRaw.text
        soup = BeautifulSoup(webData, 'lxml')

        nameBag = soup.select('#cont > section > article > h4')
        print(nameBag)

        time.sleep(1)
        # cont > section > article.clearfix.v536 > h4

        # cont > section > article.clearfix.v536.on > div > p:nth-child(1)
        # cont > section > article.clearfix.v491.on > div > p
        # cont > section > article.clearfix.v534.on > div > p

