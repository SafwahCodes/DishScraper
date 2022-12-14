from bs4 import BeautifulSoup
from typing import Union

from scrape_me import ScrapeMe
    
class ScrapeMeJO(ScrapeMe):
    
    def scrape(self, soup: BeautifulSoup) -> dict[str, Union[str, list[str]]]:
        result: dict[str, Union[str, list[str]]] = {}
        result['title'] = self.scrape_title(soup)
        result['ingredients'] = self.scrape_ingredients(soup)
        result['instructions'] = self.scrape_instructions(soup)
        return result
    
    def scrape_title(self, soup: BeautifulSoup) -> str:
        return soup.find("h1").get_text()
    
    def scrape_ingredients(self, soup: BeautifulSoup) -> list[str]:
        soup_ingredients = soup.find(class_="ingred-list")
        result: list[str] = []
        for elem in soup_ingredients.find_all("li"):
            result.append(' '.join(elem.get_text().split()))
        return result

    def scrape_instructions(self, soup:BeautifulSoup) -> list[str]:
        result: list[str] = []
        soup_instructions = soup.find(class_="recipeSteps")
        if (soup_instructions is None):
            old_instructions = soup.find(class_="method-p")
            for elem in old_instructions.find("div"):
                text = elem.getText()
                text = text.strip()
                if text:
                    result.append(text)
        else:
            
            for id, elem in enumerate(soup_instructions.find_all("li")):
                result.append(str(id+1) + ". " + elem.get_text())
        
        return result
