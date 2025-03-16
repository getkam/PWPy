from src.pom.pages.base_pom import  PageObjectModelBase

class Login(PageObjectModelBase):
    def __init__(self, page):
        super().__init__(page)

        self.user_name = self.page.locator("#loginusername")
        self.password = self.page.locator("#loginpassword")
        self.login_button = self.page.get_by_role("button", name="Log in")
        self.cancel_button = self.page.get_by_label("Log in").get_by_text("Close")

    def login(self, user_name: str, password: str):
        self.enter_credentials(user_name, password)
        self.submit_login()

    def enter_credentials(self, user_name: str, password: str):
        self.user_name.fill(user_name)
        self.password.fill(password)

    def submit_login(self):
        self.login_button.click()

    def cancel_login(self):
        self.cancel_button.click()