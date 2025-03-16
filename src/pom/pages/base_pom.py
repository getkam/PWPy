from xml.sax.xmlreader import Locator

import playwright.sync_api as playwright
from playwright.async_api import BrowserContext

from src import config


class PageObjectModelBase:
    def __init__(self, page: playwright.Page):
        self._page = page
        self._env: config.EnvConfig = config.EnvConfig()
        self._playwright: config.PlaywrightConfig = config.PlaywrightConfig()
        self._dialog_message = None

    def __getattr__(self, item):
        return getattr(self._page, item)

    @property
    def page(self):
        return self._page

    @property
    def default_url(self):
        raise NotImplementedError

    def goto(self):
        self._page.goto(self.default_url)

    def handle_dialog(self, accept=True):
        self._dialog_message = None

        def dialog_handler(dialog):
            self._dialog_message = dialog.message
            if accept:
                dialog.accept()
            else:
                dialog.dismiss()

        self._page.once("dialog", dialog_handler)

    def get_dialog_message(self, timeout: int = 5000) -> str:
        interval = 100
        already_waited = 0
        while self._dialog_message is None and already_waited < timeout:
            self._page.wait_for_timeout(interval)
            already_waited += interval
        return self._dialog_message if self._dialog_message else ""

    def get_context(self) -> BrowserContext:
        return self._page.context

