from pydantic import BaseModel

class Book(BaseModel):
    title : str
    authors : list[str]
    publish_date : str
    isbn : str

class ISBNRequest(BaseModel):
    isbn : str