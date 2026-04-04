from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvSettings(BaseSettings):
    # Core Application Settings
    PROJECT_NAME: str
    DB_URL: str


    # instruct Pydantic to look for the .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = EnvSettings()