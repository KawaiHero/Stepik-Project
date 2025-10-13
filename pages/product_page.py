import time

from .base_page import BasePage, solve_quiz_and_get_code
from .locators import ProductPageLocators

def normalize_price(text: str) -> str:
    text = text.replace('\xa0', ' ').strip()
    if text.startswith('£'):
        text = text[1:].strip() + ' £'
    return text

class ProductPage(BasePage):
    def add_product_to_cart(self):
        product_button = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON)
        product_button.click()
        solve_quiz_and_get_code(self)

    def should_be_same_price(self):
        bucket_price = self.browser.find_element(*ProductPageLocators.BUCKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        bucket_price = normalize_price(bucket_price)
        product_price = normalize_price(product_price)
        assert product_price == bucket_price, "The product price is incorrect"

    def should_be_same_pruduct_name(self):
        product_name_in_bucket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BUCKET).text
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_bucket == product_name_on_page, "The product name is incorrect"
