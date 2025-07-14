
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker # create the session


database_url = "sqlite:///./db/sentiment_analysis.db"

engine = create_engine(database_url)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base() # orm

class Text(Base):
    __tablename__ = 'texts'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    # label = Column(String, nullable=False)
    # score = Column(Float, nullable=False)


def init_db():
    Base.metadata.create_all(bind=engine)
