import pydantic_settings

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
    demoblaze_ui_url: str
    demoblaze_user: str
    demoblaze_password: str