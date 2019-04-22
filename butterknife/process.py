from bs4 import BeautifulSoup

class Processor(object):
	"""A Processor is a series of actions taken on bs4 output. These typically take a list of  objects, run the filters/transforms on them, then output a similar list that can then have another set of actions run on it."""
	def __init__(self, bs4in, chaindefinition, chainconfig={}):
		"""Takes the initial object list and a list of strings with the action names. Chain config allows for dictionary values to be set to configure individual actions."""
		self.bs4in = bs4in
		self.actiondefinitions ={
			"empty": self.EmptyAction,
			"body":self.BodyAction
		}
		self.chain=[self.actiondefinitions[act] for act in chaindefinition] 
	def EmptyAction(self, inlist):
		"""Action that returns the list originally sent to it."""
		return inlist
	def BodyAction(self, inlist):
		"""Returns the body of the list objects."""
		return [i.find_all("body")[0] for i in inlist]
	def run(self, text=False):
		"""Executes the actions in order on the stored object, then returns a new object. It's worth noting that there isn't any reason why working copies can't be chained together EXCEPT is text is set to True. If it is set to True it only outputs the text content of the working copy."""
		workingcopy = self.bs4in
		for act in self.chain:
			workingcopy=[act(initem) for initem in bs4in]
		if text: return workingcopy.text
		else: return workingcopy
		
