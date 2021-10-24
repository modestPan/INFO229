from sqlalchemy.orm import Session

from . import models, scheme

def get_news_by_date(db: Session, date_: str = '2021-01-01', limit: int = 10):
    bydate = db.query(models.News).filter(models.News.date == date_).limit(limit).all()
    return bydate

def get_news_btw_dates(db: Session, from_ : str= '2021-01-01', to_: str = '2021-01-31', limit: int = 10):
    bydate = db.query(models.News).filter(models.News.date >= from_, models.News.date <= to_).limit(limit).all()
    return bydate

def get_news_by_category(db: Session, cat_: str = 'sport'):
    bycat = db.query(models.News).join(models.Has_category).filter(models.Has_category.value == cat_).all()
    return bycat

def get_news_by_date_and_category(db: Session, from_ : str= '2021-01-01', to_: str = '2021-01-31', cat_: str = 'sport', limit: int = 10):
    bydate = db.query(models.News).join(models.Has_category).filter(models.Has_category.value == cat_).all()
    bycatanddate = db.query(models.News).join(models.Has_category).filter(models.Has_category.value == cat_).filter(models.News.date >= from_, models.News.date <= to_).all()
    return bycatanddate