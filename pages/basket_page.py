from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
   def should_be_empty_basket(self):
       self.should_be_without_product_basket_page()
       self.should_be_empty_basket_text()
       self.should_be_basket_url()


   def should_be_without_product_basket_page(self):
        continue_button = self.browser.find_element(*BasketPageLocators.CONTINUE_BUTTON)
        assert continue_button.is_displayed(), "Coupon link is not displayed, the basket is not empty"

   def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "It looks like you are not on basket page!"

   def should_be_empty_basket_text(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert 'empty' in text, "The basket is not empty"