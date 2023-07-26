from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config


engine = create_engine(config.DB.DEV_URL, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

session = Session()
