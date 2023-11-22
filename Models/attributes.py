from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Attribute(Base):
    __tablename__ = 'Attribute'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String, nullable=True)
    value = Column(String, nullable=False)
    unitedValue = Column(Integer, nullable=True)
