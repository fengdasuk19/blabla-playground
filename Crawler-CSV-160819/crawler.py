from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import time
import random

originURLroot = 'http://yenchingacademy.org/list/6/date/2017/p/'

with open('test.txt', 'w') as testfile:
    for iDigit in range(1, 13 + 1):
        # Crawling
        originURL = originURLroot + str(iDigit)
        webDataRaw = requests.get(originURL)
        webData = webDataRaw.text
        soup = BeautifulSoup(webData, 'lxml')

        nameBagRaw = soup.select('#cont > section > article > h4')
        bioBagRaw = soup.select('#cont > section > article > div > p')

        nameBag = [i.get_text() for i in nameBagRaw]
        bioBag = [i.get_text() for i in bioBagRaw]
        for nameItem, bioItem in zip(nameBag, bioBag):
            testfile.write(nameItem)
            testfile.write(', ')
            testfile.write(bioItem)
            testfile.write('\n')

        print('Succeed for page {}.\n'.format(iDigit))

        time.sleep(random.randint(1, 5))