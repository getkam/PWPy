import pytest
from playwright.sync_api import Playwright, Page

from src.config import PlaywrightConfig, EnvConfig
from src.pom.pages.home_page import HomePage
from src.pom.pages.product_page import ProductPage


@pytest.fixture(scope="session")
def playwright_config() -> PlaywrightConfig:
    return PlaywrightConfig()


@pytest.fixture(scope="session")
def env_config() -> EnvConfig:
    return EnvConfig()

@pytest.fixture()
def product_page(page:Page) -> ProductPage:
    product_page = ProductPage(page)
    return product_page

@pytest.fixture
def home_page(page: Page) -> HomePage:
    home_page = HomePage(page)
    home_page.goto()
    return home_page


@pytest.fixture(scope="session")
def context_creation(playwright_config, env_config, playwright:Playwright):
    browser = playwright.chromium.launch(headless=playwright_config.headless)
    #browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    home_page = HomePage(page)
    home_page.goto()
    login_modal = home_page.open_login_modal()
    login_modal.login(env_config.demoblaze_user, env_config.demoblaze_password)
    yield context
    page.close()
    browser.close()


@pytest.fixture
def login_set_up(context_creation):
    page = context_creation.new_page()
    home_page = HomePage(page)
    home_page.goto()
    home_page.reload()
    yield home_page
    page.close()
