from repositories.book_repository import BookRepository

class BookHandler:

    def show_all_book(self):
        books = BookRepository.get_all_book()
        for book in books:
            print(book['id'], book['title'])
