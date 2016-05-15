#coding: utf-8
'''
[Intro]
This python script is written to help you analyse data from mp.toutiao.com.
This is a beta version, which can only tell you which article was read by most users and how many times this article was read.

[Usage]
You must save the website 'Update manually' and 'Update automatically'  as 'Webpage, Complete' from mp.toutiao.com firstly.
Then you should name them 'update01.html' and 'update02.html',
and put them in the directory where this python script runs.
'''
from bs4 import BeautifulSoup

results = []
rawReading = []
statReading = []
titles = []

# count update01.html
finPath = './update01.html'

with open(finPath, 'r') as fin:
    Soup = BeautifulSoup(fin.read(), 'lxml')
    rawReading.extend([((iR.get_text())[3:]) for iR in Soup.select('body > div#scontent > div:nth-of-type(1) > div.stage > div#pagelet-list > \
div.essay-wrapper > div > div > ul > li:nth-of-type(2) > span:nth-of-type(1)')])
    titles.extend([(iTitle.get_text()) for iTitle in Soup.select('body > div#scontent > div:nth-of-type(1) > div.stage > div#pagelet-list > \
div.essay-wrapper > div > div > div:nth-of-type(1) > a')])

# count update02.html
finPath = './update02.html'

with open(finPath, 'r') as fin:
    Soup = BeautifulSoup(fin.read(), 'lxml')
    rawReading.extend([((iR.get_text())[3:]) for iR in Soup.select('body > div#scontent > div:nth-of-type(1) > div.stage > div#pagelet-list > \
div.essay-wrapper > div > div > ul > li:nth-of-type(2) > span:nth-of-type(1)')])
    titles.extend([(iTitle.get_text()) for iTitle in Soup.select('body > div#scontent > div:nth-of-type(1) > div.stage > div#pagelet-list > \
div.essay-wrapper > div > div > div:nth-of-type(1) > a')])

# print all to test

for iR in rawReading:

    if (u'万' in iR):
        iR = iR.strip(u'万')
        iR = int(float(iR) * 10000)
    else:
        iR = int(iR)

    statReading.append(iR)

for idx in range(0, len(statReading)):
    unit = {
        'title': titles[idx],
        'read': statReading[idx]
    }
    results.append(unit)

maxResult = results[0]
for iResult in results:
    if (maxResult['read'] < iResult['read']):
        maxResult = iResult

for item in maxResult:
    print(maxResult[item])