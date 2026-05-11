import json


class BookRepository:

    @staticmethod
    def read_file():
        with open("data/books.json") as f:
            return json.loads(f.read())

    @staticmethod
    def get_all_book():
        return BookRepository.read_file()
    