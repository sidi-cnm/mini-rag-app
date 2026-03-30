from pydantic_settings import BaseSettings, SettingsConfigDict




class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    File_Allowwed_types : list[str]
    File_max_size: int
    File_chunk_size: int

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()        