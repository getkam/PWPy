from src.pom.components.header_component import Header
from src.pom.pages.base_pom import PageObjectModelBase

class ProductPage(PageObjectModelBase):
    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        self.product_image = self._page.locator(".product-image > img")
        self.product_name = self._page.locator("h2")
        self.product_price = self._page.locator("h3.price-container")
        self.product_description = self._page.locator("#more-information > p")
        self.add_to_cart = self._page.get_by_role("link", name="Add to cart")

    def page(self):
        return self._page

    def click_add_to_cart(self):
        self.add_to_cart.click()



