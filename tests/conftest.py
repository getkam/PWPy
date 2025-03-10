import pytest
import playwright.sync_api as playwright

from src.config import PlaywrightConfig, EnvConfig
from src.pom.demoblazer_pom import Demoblazer
from src.pom.pages.home_page import HomePage


@pytest.fixture
def playwright_config() -> PlaywrightConfig:
    return PlaywrightConfig()

@pytest.fixture
def env_config() -> EnvConfig:
    return EnvConfig()

@pytest.fixture
def demoblazer(page: playwright.Page) -> Demoblazer:
    return Demoblazer(page=page)

@pytest.fixture
def home_page(demoblazer:Demoblazer) -> HomePage:
    demoblazer.home_page.goto()
    return demoblazer.home_page

@pytest.fixture
def login_set_up(home_page, env_config):
    home_page.open_login_modal()
    home_page.enter_credentials(env_config.demoblaze_user, env_config.demoblaze_password)
    home_page.submit_login()
    return home_page