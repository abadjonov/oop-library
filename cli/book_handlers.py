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
        print(f'Book {book_id} borrowed successfully.')
    
    def return_book(self, user):
        borrows = BorrowRepository.get_user_borrows(user.id)
        if not borrows:
            print('Sizda hozircha hech qanday kitob yo‘q.')
            return

        print('Siz qarzdor bo‘lgan kitoblar:')
        for borrow in borrows:
            print(borrow['book_id'])

        book_id = input('Return qilish uchun kitob id sini kiriting: ')
        if BorrowRepository.delete_borrow(user.id, book_id):
            print(f'Book {book_id} return qilindi!')
        else:
            print('Bunday id da qarzdorlik topilmadi.')
