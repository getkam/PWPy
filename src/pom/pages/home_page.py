from playwright.sync_api import expect

from src.pom.components.header_component import Header
from src.pom.components.login_modal import Login

from src.pom.pages.base_pom import PageObjectModelBase

class HomePage(PageObjectModelBase):
    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        # HomePage locators

        self.phone_category = self.page.get_by_role("link", name="Phones")
        self.laptops_category = self.page.get_by_role("link", name="Laptops")
        self.monitors_category = self.page.get_by_role("link", name="Monitors")

        self.products = self.page.locator(".card")

    @property
    def default_url(self):
        return self._env.demoblaze_ui_url

    def open_login_modal(self):
        self.header.click_login()
        return Login(self._page)

    def click_on_product(self, name: str):
        product_card = self.products.filter(has_text = name).first
        product_card.locator("a.hrefch").click()


