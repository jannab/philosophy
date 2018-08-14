#!/usr/bin/python
import sys
import requests
from bs4 import BeautifulSoup
from random import randint

def getNumberOfHopsToPhilosophy(url=None):
    validUrl = replaceUrlWithRandomWikiIfNotValid(url)
    return withValidUrlGetNumberOfHopsToPhilosophy(validUrl)

def replaceUrlWithRandomWikiIfNotValid(url):
    if url is None:
        return 'http://en.wikipedia.org/wiki/Special:Random'

def withValidUrlGetNumberOfHopsToPhilosophy(url):
    numberOfHops = 0
    maxNumberOfHops = 100
    content = getContentForUrl(url)
    while(checkIfCurrentIsPhilosophy(content) is False):
        if numberOfHops == maxNumberOfHops:
            return maxNumberOfHopsReached(maxNumberOfHops)
        content = cleanUpContent(content)
        numberOfHops += 1
    print(numberOfHops)
    return numberOfHops

def getContentForUrl(url):
    r = requests.get(url, timeout=10)
    print('Checking law for: '+ r.url)
    htmlParser = BeautifulSoup(r.text, 'html.parser')
    if htmlParser is None:
        print('Heres a problem in getContentForUrl')
    return htmlParser

def checkIfCurrentIsPhilosophy(content):
    if content.find(id='firstHeading').text == 'Philosophy':
        return True
    return False

def maxNumberOfHopsReached(maxNumberOfHops):
    print('The maximal number of hops ' + str(maxNumberOfHops) + ' is reached.')
    return None

def cleanUpContent(content):
    # TODO: replace
    return content
