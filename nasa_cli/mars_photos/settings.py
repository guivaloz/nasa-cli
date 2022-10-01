"""
Settings Mars Photos
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings"""

    api_key: str
    base_url: str = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    timeout: int

    class Config:
        """Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Get settings"""
    return Settings()
