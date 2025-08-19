from pydantic import BaseModel

class Book(BaseModel):
    title : str
    authors : list[str]
    publish_date : str | None
    isbn : str
