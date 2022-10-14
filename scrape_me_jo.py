from bs4 import BeautifulSoup

from scrape_me import ScrapeMe
    
class ScrapeMeJO(ScrapeMe):
    
    def scrape_title(self, soup: BeautifulSoup) -> str:
        return soup.find("h1").get_text()
    
    def scrape_ingredients(self, soup: BeautifulSoup) -> list[str]:
        soup_ingredients = soup.find(class_="ingred-list")
        result: list[str] = []
        for elem in soup_ingredients.find_all("li"):
            result.append(' '.join(elem.get_text().split()))
        return result

    def scrape_instructions(self, soup:BeautifulSoup) -> list[str]:
        soup_instructions = soup.find(class_="recipeSteps")
        result: list[str] = []
        #result.append(soup_instructions)
        for id, elem in enumerate(soup_instructions.find_all("li")):
            result.append(str(id+1) + ". " + elem.get_text())
        return result