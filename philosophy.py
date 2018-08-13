from random import randint

def getNumberOfHopsToPhilosophy(url=None):
    validUrl = replaceUrlWithRandomWikiIfNotValid(url)
    randomNumber = randint(1,100)
    if randomNumber % 10 == 0:
        return None
    return randomNumber

def replaceUrlWithRandomWikiIfNotValid(url):
    if url is None:
        return 'http://en.wikipedia.org/wiki/Special:Random'
