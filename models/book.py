from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from pydantic import validator
import datetime as dt


class BookBase(SQLModel):
    title: str = Field(index=True)
    author: str = Field(index=True)
    isbn: str = Field(unique=True, index=True)
    published_year: int
    price: float
    stock: int
    available: bool = True

    @validator("published_year")
    def validate_year(cls, v):
        current_year = dt.datetime.now().year
        if v < 1000 or v > current_year:
            raise ValueError("Invalid year")
        return v

    @validator("price")
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v

    @validator("stock")
    def validate_stock(cls, v):
        if v < 0:
            raise ValueError("Stock cannot be negative")
        return v


class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BookCreate(BookBase):
    pass


class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    published_year: Optional[int] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    available: Optional[bool] = None