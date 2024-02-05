import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from typing import List, Dict, Union

class Flat:
    def __init__(self) -> None:
        self.id = None
        self.name = None
        self.price = None
        self.additional_price = None
        self.modified = None
        self.building_state = None
        self.ownership = None
        self.floor = None
        self.size = None
        self.terrace = None
        self.move_in_date = None
        self.water_supply = None
        self.wastewater_supplier = None
        self.telecom = None
        self.electricity = None
        self.transport = None
        self.road_type = None
        self.elevator = None
        self.parking = None

class Site:
    def __init__(self, name:str) -> None:
        self.name = name
        self.base = None
        self.rental_listing_suffix = None
        self.paging_suffix = None
        self.search = None
        self.contract_type = None
        self.property_type = None
        self.location = None
        self.size = None

    def fill_with_config_data(self) -> None:    
        with open("site_urls.json", "r") as file:
            config = json.load(file)
            self.base = config[self.name]["base"]
            self.rental_listing_suffix = config[self.name]["rental_listing_suffix"]
            self.paging_suffix = config[self.name]["paging_suffix"]
            self.contract_type = config[self.name]["contract_type"]
            self.property_type = config[self.name]["property_type"]
            self.location = config[self.name]["location"]
            self.size = config[self.name]["size"]
            
        

def get_links_from_page(url:str, site:Site, driver:webdriver) -> List[str]:
    
    driver.get(url)
    sleep(5)
    tags = driver.find_elements(by=By.TAG_NAME, value="a")

    listings = set()
    for tag in tags:
        link = tag.get_attribute("href")
        if not link:
            continue
        if site.rental_listing_suffix in link and link not in listings:
            listings.add(link)
    return list(listings)


def process_listing(html:str) -> Flat:
    pass

def process_site(name:str, pages:Union[str, int]) -> List[Flat]:
    site_info = Site(name)
    site_info.fill_with_config_data()
    chrome_options = Options()
    #chrome_options.add_argument("--headless=new")
    chrome_options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=chrome_options)

    listing_links = []

    print(get_links_from_page("https://www.sreality.cz/hledani/pronajem/byty/brno?velikost=2%2Bkk", site_info, driver))
    return
    if pages == "all":
        end_of_list_flag = False
        current_page = 1
        url = ""
        while not end_of_list_flag:
            get_links_from_page(url, site_info, driver)
        else:
            pass

def main() -> None:
    
    #print(process_page("https://en.wikipedia.org/wiki/Human_spaceflight"))
    process_site("sreality", "all")


if __name__ == "__main__":
    main()
