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
        self.name_of_user = self.page.locator("#nameofuser")

    @property
    def default_url(self):
        return self._env.demoblaze_ui_url

    def login(self):
        try:
            self.login_link.click()
            self.user_name.fill(self._env.demoblaze_user)
            self.password.fill(self._env.demoblaze_password)
            self.login_button.click()
        except Exception as e:
            raise RuntimeError(f"Log In error: {e}")

    def is_logged_in(self) -> bool:
        try:
            expect(self.name_of_user).to_be_visible()
            return True
        except AssertionError:
            return False