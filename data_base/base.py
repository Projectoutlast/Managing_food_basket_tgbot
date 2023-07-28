from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config


engine = create_engine(config.DB.URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
