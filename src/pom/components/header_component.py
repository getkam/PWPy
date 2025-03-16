
from src.pom.pages.base_pom import PageObjectModelBase

class Header(PageObjectModelBase):
    def __init__(self,page):
        super().__init__(page)

        self.logo = self._page.locator("#nava")
        self.home = self._page.get_by_role("link", name="Home")
        self.contact = self._page.get_by_role("link",name="Contact")
        self.about = self._page.get_by_role("link", name="About us")
        self.cart = self._page.locator("#cartur")
        self.login = self._page.get_by_role("link", name="Log in")
        self.signup = self._page.locator("#signin2")
        self.logout = self._page.get_by_role("link", name="Log out")
        self.username = self._page.locator("#nameofuser")

    def click_logo(self):
        self.logo.click()

    def click_contact(self):
        self.contact.click()

    def click_about(self):
        self.about.click()

    def click_cart(self):
        self.cart.click()

    def click_login(self):
        self.login.click()

    def click_signup(self):
        self.signup.click()

    def click_logout(self):
        self.logout.click()

    def get_user_name(self):
        welcome_text =  self.username.inner_text()
        parts = welcome_text.split(" ", 1)
        if len(parts) > 1:
            return parts[1]
        else:
            return ""

    def is_logged_in_as(self, username):

        self.username.wait_for(timeout=5000)
        welcome_text = self.username.inner_text()


        parts = welcome_text.split(" ", 1)
        if len(parts) == 2:
            actual_username = parts[1].strip()
            return actual_username.lower() == username.lower()
        return False

