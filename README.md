# Getting to Philosophy

This project tests the "Getting to Philosophy law":
> Clicking on the first link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, would usually lead to the Philosophy article. As of February 2016, 97% of all articles in Wikipedia eventually led to the article Philosophy. ([Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy))

## Getting Started

Install dependencies:
```
pip install -r requirements.txt
```

Test the law for a given Wikipedia link (will use a random Wikipedia link if no valid link passed):
```
python philosophy.py WIKIPEDIA_URL
```

Test the law for 10 random wikipedia pages:
```
python test.py
```
