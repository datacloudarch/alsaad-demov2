from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AL Saad Analytics API"
    environment: str = "development"
    database_url: str = ""  # e.g. mssql+pyodbc:///?odbc_connect=...

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


