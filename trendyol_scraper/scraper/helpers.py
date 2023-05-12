import logging
from trendyol_scraper.utils.scrapper import ProductScraper
from rest_framework.response import Response

logger = logging.getLogger(__name__)


def is_true_url(url: str):
    return True if "trendyol.com" in url else False


product_scraper = ProductScraper()


class ProductSaveHelpers:

    @classmethod
    def __save_merchant(cls, merchant_name: str, url: str, score: float):
        from .models import Merchant
        merchant = Merchant(merchant_name=merchant_name, merchant_url=url, score=score)
        merchant.save()

        return merchant

    @classmethod
    def __save_product(cls, **kwargs):
        from .models import Product
        product = Product(**kwargs)
        product.save()

        return product.id

    def save_product_details(self, url: str):

        product_details = product_scraper.scrape_product(url=url)

        if not product_details:
            return Response("Something Wrong", status=500)

        merchant_name = product_details.pop("merchant_name", "")
        merchant_url = product_details.pop("merchant_url", "")

        merchant_details = product_scraper.scrape_merchant(url=f"https://www.trendyol.com{merchant_url}")

        if not all([merchant_name, merchant_url]):
            return Response("Merchant Not Parsed", status=500)

        merchant = self.__save_merchant(
            merchant_name=merchant_name,
            url=merchant_url,
            score=float(merchant_details["score"])
        )
        product_details["merchant_id"] = merchant
        product_id = self.__save_product(**product_details)

        return Response(f"Succesfully Inserted. Product ID:{product_id}", status=200)


