from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import select
from typing import List, Optional, Any, cast

from models.book import Book, BookCreate, BookUpdate
from database.session import engine, get_session
from sqlmodel import SQLModel, Session

app = FastAPI()


# creating tables
SQLModel.metadata.create_all(engine)


#Creating a book
@app.post("/books", response_model=Book)
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    db_book = Book.from_orm(book)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


# Get all books 
@app.get("/books", response_model=List[Book])
def get_books(
    author: Optional[str] = None,
    title: Optional[str] = None,
    session: Session = Depends(get_session),
):
    query = select(Book)

    if author:
        query = query.where(cast(Any, Book.author).contains(author))
    if title:
        query = query.where(cast(Any, Book.title).contains(title))

    books = session.exec(query).all()
    return books


# Get one book
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


#Updating a book
@app.patch("/books/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookUpdate, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    updates = data.dict(exclude_unset=True)

    for key, value in updates.items():
        setattr(book, key, value)

    from datetime import datetime
    book.updated_at = datetime.utcnow()

    session.add(book)
    session.commit()
    session.refresh(book)

    return book


# Deleting a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    session.delete(book)
    session.commit()

    return {"message": "Book deleted"}
    

# Searching for a book by title or author
@app.get("/books/search", response_model=List[Book])
def search_books(q: str, session: Session = Depends(get_session)):
    query = select(Book).where(
        (cast(Any, Book.title).contains(q)) | (cast(Any, Book.author).contains(q))
    )
    return session.exec(query).all()