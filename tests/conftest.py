import pytest
from playwright.sync_api import Playwright, Page

from src.config import PlaywrightConfig, EnvConfig
from src.pom.pages.cart_page import CartPage
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

@pytest.fixture()
def home_page(page: Page) -> HomePage:
    home_page = HomePage(page)
    home_page.goto()
    return home_page


@pytest.fixture(scope="session")
def context_creation(playwright_config, env_config, playwright: Playwright):
    browser = playwright.chromium.launch(headless=playwright_config.headless)
    #browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    yield context
    context.close()
    browser.close()


@pytest.fixture()
def login_set_up(context_creation, env_config):
    page = context_creation.new_page()
    home_page = HomePage(page)
    home_page.goto()
    login_modal = home_page.open_login_modal()
    login_modal.login(env_config.demoblaze_user, env_config.demoblaze_password)
    yield home_page
    page.close()


@pytest.fixture()
def clear_cart(login_set_up):
    home_page = HomePage(login_set_up.page)
    home_page.header.click_cart()
    cart_page = CartPage(home_page.page)
    cart_page.page.wait_for_load_state("networkidle")
    cart_page.clear_cart()
    cart_page.header.click_home()
