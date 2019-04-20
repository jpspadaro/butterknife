# butterknife
A simple web scraping library for python3 utilizing BeautifulSoup

## Basic Usage
Example:
```
>>> from bs4 import BeautifulSoup
>>> from butterknife.scrape import Scrape
>>> example_scrape=Scrape(["https://en.wikipedia.org/wiki/List_of_sequenced_animal_genomes","https://en.wikipedia.org/wiki/List_of_sequenced_archaeal_genomes"])
>>> example_scrape.SoupifyAll()
>>> print ([i['url'] for i in example_scrape.pages])
['https://en.wikipedia.org/wiki/List_of_sequenced_animal_genomes', 'https://en.wikipedia.org/wiki/List_of_sequenced_archaeal_genomes']
>>> bodyout0=example_scrape.pages[0]['html'].select('body')
>>> bodyout0[0].text[:100]
'\n\n\n\n\n\n\n\nList of sequenced animal genomes\n\nFrom Wikipedia, the free encyclopedia\n\n\nJump to navigation'
```
Individual pages can use the PagePull object to get the source html as one large string.

```
>>> from butterknife.scrape import PagePull>>> page_test=PagePull("https://en.wikipedia.org/wiki/List_of_sequenced_archaeal_genomes")
>>> print(page_test.htmlcontent[:100])
b'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title'
>>> str(page_test)[:100]
'<!DOCTYPE html>\n<html class="client-nojs" lang="en" dir="ltr">\n<head>\n<meta charset="UTF-8"/>\n<title'
>>> 
```
