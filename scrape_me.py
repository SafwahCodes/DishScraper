import requests
from bs4 import BeautifulSoup
from typing import Union

class ScrapeMe:
    def __init__(self):
        pass
    
    def fetch(self, url: str) -> requests.models.Response:
        return requests.get(url)
    
    def convert_to_bs4(self, response: requests.models.Response, parser: str="html.parser") -> BeautifulSoup:
        return BeautifulSoup(response.content, features=parser)
    
    def scrape(self, soup: BeautifulSoup) -> dict[str, Union[str, list[str]]]:
        result: dict[str, Union[str, list[str]]] = {}
        result['title'] = self.scrape_title(soup)
        result['ingredients'] = self.scrape_ingredients(soup)
        result['instructions'] = self.scrape_instructions(soup)
        return result
    
    def scrape_title(self, soup: BeautifulSoup) -> str:
        raise NotImplementedError
    
    def scrape_ingredients(self, soup: BeautifulSoup) -> list[str]:
        raise NotImplementedError

    def scrape_instructions(self, soup:BeautifulSoup) -> list[str]:
        raise NotImplementedError