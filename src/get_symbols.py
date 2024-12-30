import requests
from bs4 import BeautifulSoup

class DataIngestion():	
	def __init__(self, url_link, headers):
		self.url_link = url_link
		self.headers = headers
	
	@property
	def get_data(self):
		response = requests.request("GET", self.url_link, headers=self.headers)
		soup = BeautifulSoup(response.content, "html.parser")
		symbols = []
		for symbol in soup.find_all(class_="Fw(b)", attrs={"data-test":"symbol-link"}):
			symbols.append(symbol.text)
		return symbols		
	
	
