from fastapi import FastAPI
from library import book, library
import uvicorn

l_api = FastAPI()
lib = library()

@l_api.get('/books/')
async def get_all():
    return lib

@l_api.get('/books/{id}')
async def get_book(id: int):
    return lib.get_book(id)

@l_api.post('/books/')
async def new_book(title: str, author: str, year: int):
    id = lib.make_id()
    my_book = book(id, title, author, year)
    lib.add_book(id, my_book)
    return my_book

@l_api.put('/books/{id}')
async def update_book(id: int, title: str, author: str, year: int):
    lib.add_book(id, book(id, title, author, year))

@l_api.delete('/books/{id}')
async def delete_book(id: int):
    lib.delete_book(id)

if __name__ == '__main__':
    uvicorn.run('api:l_api')