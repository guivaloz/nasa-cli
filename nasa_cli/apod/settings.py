"""
Settings
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings"""

    api_key: str
    base_url: str = "https://api.nasa.gov/planetary/apod"
    timeout: int

    class Config:
        """Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Get settings"""
    return Settings()
