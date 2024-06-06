import random

class book:
    def __init__(self, id: int, title: str, author: str, year: int):
        self.id = id
        self.title = title
        self.author = author
        self.year = year


class library:
    def __init__(self):
        self.storage = dict()

    def add_book(self, id: int, book):
        self.storage[id] = book
        return book

    def get_all_books(self):
        return self.storage

    def get_book(self, id: int):
        return self.storage.get(id)

    def delete_book(self, id: int):
        del self.storage[id]

    def make_id(self):
        id = round(random.random() * 10000000000000)
        if id in self.storage:
            return self.make_id()
        return id