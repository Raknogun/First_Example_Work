from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        self.should_add_to_basket()

    def should_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_TO_ADD).text == self.browser.find_element(*ProductPageLocators.ITEM_BOUGHT).text, "Added different item"
