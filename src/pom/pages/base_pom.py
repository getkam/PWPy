import playwright.sync_api as playwright
from src import config

class PageObjectModelBase:
    def __init__(self, page: playwright.Page):
        self._page = page
        self._env: config.EnvConfig = config.EnvConfig()
        self._playwright: config.PlaywrightConfig = config.PlaywrightConfig()

    @property
    def page(self):
        return self._page

    @property
    def default_url(self):
        raise NotImplementedError

    def goto(self):
        self._page.goto(self.default_url)