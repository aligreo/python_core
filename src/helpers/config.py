
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPEN_ROUTER_MODEL_ID: str = "qwen/qwen3-8b:free"
    OPEN_ROUTER_API_KEY: str = "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"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Settings()