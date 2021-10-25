from typing import List, Optional

from pydantic import BaseModel


class has_categoryBase(BaseModel):
    value: str

class has_categoryCreate(has_categoryBase):
    pass

class has_category(has_categoryBase):
    id: int
    value: str
    class Config:
        orm_mode = True


class newsBase(BaseModel):
    title: str
    url: str
    date: str
    media_outlet: str
    

class newsCreate(newsBase):
    pass

class news(newsBase):
    id: int
    category: List[has_category] = []
    class Config:
        orm_mode = True