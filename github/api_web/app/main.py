## Ejecutar. 
# uvicorn my-api.main:app --reload
# iniciar MySQL
# mysql -u root -p
# sudo service mysql start

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, scheme
from .database import SessionLocal, engine, session

# Se elimina y se crean las tablas
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

# llenarse de datos

new1 = models.News(title = 'n1', date = '2021-01-01', url = 'n1', media_outlet = 'n1')
new2 = models.News(title = 'n2', date = '2021-01-05', url = 'n2', media_outlet = 'n2')
new3 = models.News(title = 'n3', date = '2021-01-15', url = 'n3', media_outlet = 'n3')
new4 = models.News(title = 'n4', date = '2021-01-20', url = 'n4', media_outlet = 'n4')
new5 = models.News(title = 'n5', date = '2021-01-31', url = 'n5', media_outlet = 'n5')

session.add(new1)
session.add(new2)
session.add(new3)
session.add(new4)
session.add(new5)

session.commit()

cat1 = models.Has_category(value = 'sport', owner = new1)
cat2 = models.Has_category(value = 'comedy', owner = new1)
cat3 = models.Has_category(value = 'sport', owner = new3)
cat4 = models.Has_category(value = 'crime', owner = new2)
cat5 = models.Has_category(value = 'funny', owner = new4)
cat6 = models.Has_category(value = 'crime', owner = new5)

session.add(cat1)
session.add(cat2)
session.add(cat3)
session.add(cat4)
session.add(cat5)
session.add(cat6)

session.commit()


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/news/", response_model=List[scheme.news])
def read_news(date_: str = '2021-01-01', limit: int = 10, db: Session = Depends(get_db)):
    news = crud.get_news_by_date(db, date_ = date_, limit=limit)
    return news
 
@app.get("/news/range/", response_model=List[scheme.news])
def read_news(from_: str = '2021-01-01', to_: str = '2021-01-31', limit: int = 10, db: Session = Depends(get_db)):
    news = crud.get_news_btw_dates(db, from_ = from_, to_ = to_, limit=limit)
    return news

 
@app.get("/news/cat/", response_model=List[scheme.news])
def read_news(cat_: str = 'category', db: Session = Depends(get_db)):
    news = crud.get_news_by_category(db, cat_ = cat_)
    return news
    
@app.get("/v1/news", response_model=List[scheme.news])
def read_news(from_: str = '2021-01-01', to_: str = '2021-01-31', cat_: str = 'category', limit: int = 10, db: Session = Depends(get_db)):
    news = crud.get_news_by_date_and_category(db, from_ = from_, to_ = to_, cat_ = cat_, limit = limit)
    return news
