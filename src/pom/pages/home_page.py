from playwright.sync_api import expect
from src.pom.pages.base_pom import PageObjectModelBase

class HomePage(PageObjectModelBase):
    def __init__(self, page):
        super().__init__(page)

        # HomePage locators
        self.login_link = self.page.get_by_role("link", name="Log in")
        self.user_name = self.page.locator("#loginusername")
        self.password = self.page.locator("#loginpassword")
        self.login_button = self.page.get_by_role("button", name="Log in")
        self.cancel_button = self.page.get_by_label("Log in").get_by_text("Close")
        self.name_of_user = self.page.locator("#nameofuser")

    @property
    def default_url(self):
        return self._env.demoblaze_ui_url

    def open_login_modal(self):
        self.login_link.click()

    def enter_credentials(self, user_name:str, password:str):
        self.user_name.fill(user_name)
        self.password.fill(password)

    def submit_login(self):
        self.login_button.click()

    def cancel_login(self):
        self.cancel_button.click()

    def is_logged_in(self) -> bool:
        try:
            expect(self.name_of_user).to_be_visible()
            return True
        except AssertionError:
            return False



