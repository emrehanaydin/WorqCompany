import requests
import logging

from bs4 import BeautifulSoup

logger = logging.getLogger("Scrapper")


class ProductScraper:
    def __init__(self):
        self.soup = None

    def __perform_request(self, url):
        try:
            return requests.get(url)
        except Exception as error:
            logger.error(error)

        return

    def __init_soup(self, _response):
        self.soup = BeautifulSoup(_response.content, 'html.parser')

    def __get_category_from_product_page(self):
        _categories = []
        categories = self.soup.findAll("a", {"class": "product-detail-breadcrumb-item"})

        for category in categories:
            category_name = category.text.strip()

            if category_name not in _categories:
                _categories.append(category_name)

        return ",".join(_categories)

    def scrape_product(self, url: str):
        try:
            response = self.__perform_request(url)
            self.__init_soup(_response=response)

            product_name = self.soup.find("h1", {'class': "pr-new-br"})
            brand = product_name.find("a").text.strip()
            merchant_name = self.soup.find('a', {'class': 'merchant-text'})
            merchant_url = merchant_name["href"]
            image_tag = self.soup.find('div', {"class": "gallery-container"})
            image_url = image_tag.find("img")["src"]
            price = self.soup.find('span', {'class': 'prc-dsc'}).text.strip()
            description = self.soup.find("div", {'class': "featured-information"}).text.strip()
            price, currency = price.split(" ")
            category = self.__get_category_from_product_page()

            return {
                "brand": brand,
                "product_name": product_name.text.strip(),
                "description": description,
                "price": float(price.replace(",", ".")),
                "merchant_name": merchant_name.text.strip(),
                "merchant_url": merchant_url,
                "image_url": image_url,
                "category": category

            }
        except Exception as error:
            logger.error(error)
        return

    def scrape_merchant(self, url):

        response = self.__perform_request(url)
        self.__init_soup(_response=response)

        score = self.soup.find('div', {'class': 'seller-store__score'}).text.strip()
        image = self.soup.find('img', {'class': 'seller-icon'}).text.strip()

        return {
            "score": score,
            "image": image,
        }
