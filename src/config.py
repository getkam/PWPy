from pydantic import Field
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
    demoblaze_ui_url: str = os.getenv("DEMOBLAZE_UI_URL", "https://www.demoblaze.com/index.html")
    demoblaze_user: str = os.getenv("DEMOBLAZE_USER", "default_user")
    demoblaze_password: str = os.getenv("DEMOBLAZE_PASSWORD", "default_password")