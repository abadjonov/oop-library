from repositories.book_repository import BookRepository
from repositories.borrow_repository import BorrowRepository


class BookHandler:
    def show_all_book(self):
        books = BookRepository.get_all_book()
        for book in books:
            print(book['id'], book['title'])

    def search_book(self):
        serach = input('Search: ')
        books = BookRepository.get_all_book()
        for book in books:
            if serach == book['title']:
                print(book['id'], book['title'])

    def borrow_book(self, user):
        book_id = input('Book id: ')
        BorrowRepository.create_borrow(user, book_id)
        
