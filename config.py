import os

from dataclasses import dataclass
from environs import Env


basedir = os.path.abspath(os.path.dirname(__name__))
URL = "sqlite:///" + basedir + "/bot_db.db"


@dataclass
class BotConfig:
    TOKEN: str


@dataclass
class DataBaseConfig:
    URL: str
    DEV_URL: str


@dataclass
class Config:
    TG_BOT: BotConfig
    DB: DataBaseConfig


env = Env()
env.read_env()

config = Config(TG_BOT=BotConfig(TOKEN=env("BOT_TOKEN")),
                DB=DataBaseConfig(URL=env("URL"),
                                  DEV_URL=env("DEV_URL")))
