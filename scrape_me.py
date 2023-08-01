import requests
from bs4 import BeautifulSoup
from typing import Union

## 
# @class ScrapeMe scrape_me.py
# @brief This is the ScrapeMe base class to be inherited by other classes where specific implementations will be defined.
class ScrapeMe:
	
	## The constructor.
	def __init__(self):
		pass

  ## Returns a requests.Response object from a given URL.
  # @param url The URL to get a response from.
  # @return A requests.Response object returned by sending a GET request to url.
	def fetch(self, url: str) -> requests.models.Response:
		return requests.get(url)
	
  ## Converts a requests.Response object into a BeautifulSoup object.
  # @param response A requests.Reponse object to convert.
  # @param parser Specifies the type of parsing to be done. Default parses html.
  # @return A BeautifulSoup object containing the contents of the requests.Response object.
	def convert_to_bs4(self, response: requests.models.Response, parser: str="html.parser") -> BeautifulSoup:
		return BeautifulSoup(response.content, features=parser)
	
  ## Scrapes the recipe title, ingredients and instructions from a BeautifulSoup object.
  # @param soup A BeautifulSoup object containing the recipe to scrape.
  # @return A dictionary containing the title, ingredients and instructions of the recipe.
	def scrape(self, soup: BeautifulSoup) -> dict[str, Union[str, list[str]]]:
		result: dict[str, Union[str, list[str]]] = {}
		result['title'] = self.scrape_title(soup)
		result['ingredients'] = self.scrape_ingredients(soup)
		result['instructions'] = self.scrape_instructions(soup)
		return result
			
  ## Scrapes the recipe title from a BeautifulSoup object
  # @param soup A BeautifulSoup object to scrape from.
  # @return A string representing the recipe title. Raises a NotImplementedError if not overriden in child classes.
	def scrape_title(self, soup: BeautifulSoup) -> str:
		raise NotImplementedError
			
  ## Scrapes the recipe ingredients from a BeautifulSoup object
  # @param soup A BeautifulSoup object to scrape from.
  # @return A list of strings representing the recipe ingredients. Raises a NotImplementedError if not overriden in child classes.
	def scrape_ingredients(self, soup: BeautifulSoup) -> list[str]:
		raise NotImplementedError

  ## Scrapes the recipe instructions from a BeautifulSoup object
  # @param soup A BeautifulSoup object to scrape from.
  # @return A list of strings representing the recipe instructions. Raises a NotImplementedError if not overriden in child classes.
	def scrape_instructions(self, soup:BeautifulSoup) -> list[str]:
		raise NotImplementedError
	