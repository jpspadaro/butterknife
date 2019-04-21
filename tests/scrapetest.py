from butterknife.scrape import Scrape
from pprint import pprint as pprint

"""
Scrapes some city information from wikipedia and displays them as blocks as text. Could be more formalized as a test, but good enough for now.
"""
def main():
	wikiscrape=Scrape(["https://en.wikipedia.org/wiki/Syracuse,_New_York","https://en.wikipedia.org/wiki/New_York_City","https://en.wikipedia.org/wiki/Los_Angeles"])

	wikiscrape.SoupifyAll()
	infoboxes=[i['html'].find_all("table", class_="infobox") for i in wikiscrape.pages]

	for i in infoboxes:
		print(i[0].text, "\n\n\n--------------------")

if __name__=="__main__":
	main()
