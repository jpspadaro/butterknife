from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

#Logging stuff.
import logging



class PagePull(object):
	"""Object for handling a simple http request, and if it works (200) it provides the html content."""
	def __init__(self, pageurl, PULL=True, contenttype='html'):
		self.htmlcontent=""
		self.htmlcontenttype=contenttype
		self.pageurl = pageurl
		
		#Pulls content on init by default, but still needs to init loaded as False
		self.loaded=False
		if PULL: self.loaded = self.Pull()
	def Pull(self):
		"""Tries to pull the page. If successful (gets valid html content) then it returns True. Otherwise it returns False. This value should be stored in self.loaded."""
		try:
			with closing(get(url, stream=True)) as response:
				if self.CheckResponse(response):
					self.htmlcontent=response.content
					return True
				else return False
		except RequestException as e:
			logging.warning("Could not request page %s." % pageurl)  
			return False

	def CheckResponse(self, response):
		"""Checks to see if what we got from the request is a real content or a failed response."""
		contenttype=response.headers['Content-Type'].lower()
		return (response.status_code == 200 and contenttype is not None and contenttype.find(self.htmlcontenttype) > -1)
	def __bool__(self):
		"""Just use the loaded state as the bool."""
		return self.loaded
	def __str__(self):
		"""Should in theory provide the loaded html content or an empty string (as it was initialized). An edge is when successive pulls are made from the same PagePull object - this could result in a failed pull with old content. This is a desirable fall over. If you need to confirm the content is the most current, then just check the value of loaded or the object itself first:
		
		mypull=PagePull("myurl")
		mypull.Pull()
		if mypull: mycontent=str(mypull)
		else: whatever you do if the content isn't current.
		"""
		return self.htmlcontent

class Scrape(object):
	""" The basic 'scrape' class. It aggregates multiple PagePulls, and cleans up the data a bit to make it more useful."""
	def __init__(self):
		pass
