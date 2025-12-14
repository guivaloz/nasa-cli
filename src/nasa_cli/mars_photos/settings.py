"""
Settings Mars Photos
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings"""

    API_KEY: str = ""
    BASE_URL: str = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    TIMEOUT: int = 20

    class Config:
        """Config"""

        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Get settings"""
    return Settings()
