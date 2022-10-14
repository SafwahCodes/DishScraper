import pprint

from scrape_me_bb import ScrapeMeBB

url = "https://www.budgetbytes.com/lemon-bars/"
    
scrape_me = ScrapeMeBB()
output = scrape_me.scrape(scrape_me.convert_to_bs4(scrape_me.fetch(url)))
pprint.pprint(output)