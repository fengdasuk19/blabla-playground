from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import time
import random

def writeln(f, content):
    f.write(content)
    f.write('\n')

def isFemale(rawText):
    for i in ["She ", "she ", "Her ", "her "]: # Must use SPACE following female keyword
        if i in rawText:
            return True
    return False


originURLroot = 'http://yenchingacademy.org/list/6/date/2017/p/'
nameFile = open('nameList.txt', 'a')
genderFile = open('genderList.txt', 'a')
bioFile = open('bioList.txt', 'a')

for iDigit in range(1, 13 + 1):
    # Crawling
    originURL = originURLroot + str(iDigit)
    webDataRaw = requests.get(originURL)
    webData = webDataRaw.text
    soup = BeautifulSoup(webData, 'lxml')

    nameBagRaw = soup.select('#cont > section > article > h4')
    bioBagRaw = soup.select('#cont > section > article > div') # before '#cont > section > article > div > p'
    '''
    for i in bioBagRaw:
        print(i)

    print()
    input("Enter to continue.")
    '''

    nameBag = [i.get_text() for i in nameBagRaw]
    bioBag = [i.get_text() for i in bioBagRaw]
    '''
    for i in bioBag:
        if i == '':
            bioBag.remove(i)
    print('bioBag, nameBag')
    for i in bioBag:
        print(i)
    print(len(nameBag))
    input("Enter to continue.")
    '''
    if len(nameBag) == len(bioBag):
        for name, bio in zip(nameBag, bioBag):
            writeln(nameFile, name)
            writeln(bioFile, bio)
            if isFemale(bio):
                writeln(genderFile, 'Female')
                print('Female')
            else:
                writeln(genderFile, 'Male')
                print('Male')

            print('{} finished.'.format(name))
    else:
        print('False')

    print('Succeed for page {}.\n'.format(iDigit))


'''
    for name, bio in zip(nameBag, bioBag):
        writeln(nameFile, name)
        writeln(bioFile, bio)
        if isFemale(bio):
            writeln(genderFile, 'Female')
            print('Female\n')
        else:
            writeln(genderFile, 'Male')
            print('Male\n')

        print('{} finished.'.format(name))
'''