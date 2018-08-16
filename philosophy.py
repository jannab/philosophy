#!/usr/bin/python
import sys
import requests
import re
from bs4 import BeautifulSoup
from time import sleep

MAX_NUMBER_OF_HOPS = 10
VISITED_PAGES = []

def getNumberOfHopsToPhilosophy(url=None):
    validUrl = replaceUrlWithRandomWikiIfNotValid(url)
    return withValidUrlGetNumberOfHopsToPhilosophy(validUrl)

def replaceUrlWithRandomWikiIfNotValid(url):
    if url is None or 'en.wikipedia.org' not in url:
        return handleNoPassedWikiUrl(url)
    return url

def handleNoPassedWikiUrl(url):
    print('There was no Wiki URL specified (' + str(url)
            + '), working with random Wiki Entry.')
    return 'http://en.wikipedia.org/wiki/Special:Random'

def withValidUrlGetNumberOfHopsToPhilosophy(url):
    numberOfHops = 0
    currentSoup = initializeFirstSoupAndStartStatement(url)
    while(checkIfCurrentIsPhilosophy(currentSoup) is False):
        nextUrl = getFirstValidLink(currentSoup)
        if checkIfStuck(nextUrl, numberOfHops) is True:
            return None
        numberOfHops += 1
        currentSoup = getSoupForUrl(nextUrl)
    print('Philosophy found. Number of hops: ' + str(numberOfHops))
    return numberOfHops

def initializeFirstSoupAndStartStatement(url):
    print('Checking law for:')
    currentSoup = getSoupForUrl(url)
    print('Hops:')
    return currentSoup

def getSoupForUrl(url):
    r = requests.get(url, timeout=10)
    print(r.url)
    VISITED_PAGES.append(str(r.url))
    sleep(0.5)
    return BeautifulSoup(r.text, 'html.parser')

def checkIfCurrentIsPhilosophy(currentSoup):
    if getPageTitle(currentSoup) == 'Philosophy':
        return True
    return False

def getPageTitle(currentSoup):
    return currentSoup.find(id='firstHeading').text

def checkIfStuck(nextUrl, numberOfHops):
    if numberOfHops == MAX_NUMBER_OF_HOPS:
        print('The maximal number of hops ' + str(MAX_NUMBER_OF_HOPS)
                    + ' is reached.')
    elif nextUrl is None:
        print('Stuck, no Wiki Link on the page.')
    elif nextUrl in VISITED_PAGES:
        print('Stuck in a loop, already visited: ' + str(nextUrl))
    else:
        # not stuck
        return False
    return True

def getFirstValidLink(currentSoup):
    cleanedSoup = cleanSoupFromUnwantedLinks(currentSoup)
    return getFirstLink(cleanedSoup)

def cleanSoupFromUnwantedLinks(currentSoup):
    # TODO: change
    return currentSoup

def getFirstLink(cleanedSoup):
    firstWikiLink = cleanedSoup.find('a', href = re.compile('^/wiki/'))
    fullUrl = getFullUrlFromWikiLink(firstWikiLink)
    return fullUrl

def getFullUrlFromWikiLink(wikiLink):
    return 'https://en.wikipedia.org' + wikiLink.get('href')
