import requests
from bs4 import BeautifulSoup

class DataIngestion():	
	
	@staticmethod
	def get_data(url_link, headers):
		response = requests.request("GET", url_link, headers=headers)
		soup = BeautifulSoup(response.content, "html.parser")
		symbols = []
		for symbol in soup.find_all(class_="Fw(b)", attrs={"data-test":"symbol-link"}):
			symbols.append(symbol.text)
		return symbols		
	
	
