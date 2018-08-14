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
    maxNumberOfHops = 10
    print('Checking law for:')
    currentPage = getHtmlForUrl(url)
    print('Hops:')
    while(checkIfCurrentIsPhilosophy(currentPage) is False):
        if numberOfHops == maxNumberOfHops:
            return maxNumberOfHopsReached(maxNumberOfHops)
        currentPage = updateCurrentPageToFirstLink(currentPage)
        numberOfHops += 1
    return numberOfHops

def getHtmlForUrl(url):
    r = requests.get(url, timeout=10)
    print(r.url)
    return BeautifulSoup(r.text, 'html.parser')

def checkIfCurrentIsPhilosophy(pageHtml):
    if pageHtml.find(id='firstHeading').text == 'Philosophy':
        return True
    return False

def maxNumberOfHopsReached(maxNumberOfHops):
    print('The maximal number of hops ' + str(maxNumberOfHops) + ' is reached.')
    return None

def updateCurrentPageToFirstLink(currentPage):
    firstLinkUrl = getFirstValidLink(currentPage)
    return getHtmlForUrl(firstLinkUrl)

def getFirstValidLink(pageHtml):
    # TODO: change
    return 'http://en.wikipedia.org/wiki/Special:Random'
