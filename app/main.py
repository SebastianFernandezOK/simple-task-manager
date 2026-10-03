from fastapi import FastAPI
from config import settings
from functools import lru_cache
from . import config

app = FastAPI()


@lru_cache
def get_settings():
    return config.Settings()