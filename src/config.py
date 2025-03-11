import pydantic_settings
import os


class PlaywrightConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_PLAYWRIGHT_", env_file=".env", frozen=True, extra="ignore"
    )
    headless: bool = True
    browser: str = "chromium"

class EnvConfig(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_prefix="QA_ENV_", env_file=".env", frozen=True, extra="ignore"
    )
    demoblaze_ui_url: str = os.getenv("QA_ENV_DEMOBLAZE_UI_URL", "https://www.demoblaze.com")
    demoblaze_user: str = os.getenv("QA_ENV_DEMOBLAZE_USER", "default_user")
    demoblaze_password: str = os.getenv("QA_ENV_DEMOBLAZE_PASSWORD", "")