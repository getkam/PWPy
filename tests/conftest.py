import pytest
import playwright.sync_api as playwright

from src.config import PlaywrightConfig, EnvConfig
from src.pom.demoblazer_pom import Demoblazer

@pytest.fixture
def playwright_config() -> PlaywrightConfig:
    return PlaywrightConfig()

@pytest.fixture
def env_config() -> EnvConfig:
    return EnvConfig()

@pytest.fixture
def demoblazer(page: playwright.Page) -> Demoblazer:
    return Demoblazer(page=page)
