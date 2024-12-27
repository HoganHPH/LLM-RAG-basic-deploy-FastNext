import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class CommonSettings(BaseSettings):
    APP_NAME: str = "BasicRAG"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = os.getenv("APP_HOST")
    PORT: int = os.getenv("APP_PORT")


class DatabaseSettings(BaseSettings):
    DB_URL: str = ""
    DB_NAME: str = ""


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass