from bs4 import BeautifulSoup
from typing import Union

from scrape_me import ScrapeMe
    
class ScrapeMeBB(ScrapeMe):
    def scrape(self, soup: BeautifulSoup) -> dict[str, Union[str, list[str]]]:
        result: dict[str, Union[str, list[str]]] = {}
        result['title'] = self.scrape_title(soup)
        result['ingredients'] = self.scrape_ingredients(soup)
        result['instructions'] = self.scrape_instructions(soup)
        return result
    
    def scrape_title(self, soup: BeautifulSoup) -> str:
        return soup.find(class_="wprm-recipe-name").get_text()
    
    def scrape_ingredients(self, soup: BeautifulSoup, remove_price: bool=True, separator: str='(') -> list[str]:
        soup_ingredients = soup.find(class_="wprm-recipe-ingredients-container")
        result: list[str] = []
        for elem in soup_ingredients.find_all(class_="wprm-recipe-ingredient"):
            result.append(elem.get_text().split(separator, 1)[0] if remove_price else elem.get_text())
        return result

    def scrape_instructions(self, soup:BeautifulSoup) -> list[str]:
        soup_instructions = soup.find(class_="wprm-recipe-instructions-container")
        result: list[str] = []
        for id, elem in enumerate(soup_instructions.find_all(class_="wprm-recipe-instruction")):
            result.append(str(id+1) + ". " + elem.get_text())
        return result
