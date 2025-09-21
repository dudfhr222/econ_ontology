from functools import lru_cache
from pydantic_settings import BaseSettings  # ✅ pydantic이 아니라 pydantic-settings에서 import

class Settings(BaseSettings):
    # Ollama 관련
    OLLAMA_ENDPOINT: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.1:8b"

    # CoinGecko 기본 통화
    DEFAULT_CURRENCY: str = "usd"

    # (옵션) FRED
    FRED_API_KEY: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
