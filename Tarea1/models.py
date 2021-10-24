from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, INTEGER
from sqlalchemy.orm import backref, relation, relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

#Considerando relacion N - 1
class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, index=True)
    date = Column(String(50), unique=True, index=True)
    url = Column(String(50), unique=True, index=True)
    media_outlet = Column(String(50), unique=True, index=True)
    category = relationship("Has_category",backref="owner")


class Has_category(Base):
    __tablename__ = "has_category"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(50), unique=False, index=True)
    owner_id = Column(Integer, ForeignKey('news.id'))


