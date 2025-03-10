import playwright.sync_api as playwright
from src.pom.pages.home_page import HomePage

class Demoblazer:
    def __init__(self, page: playwright.Page):
        self.home_page: HomePage = HomePage(page)