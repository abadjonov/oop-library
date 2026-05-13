import json
from uuid import uuid1


class BorrowRepository:
    @staticmethod
    def read_file():
        with open("data/borrow.json") as f:
            return json.loads(f.read())
        
    @staticmethod
    def save_file(borrows):
        with open("data/borrow.json", "w") as f:
            f.write(json.dumps(borrows, indent=4))

    @staticmethod
    def create_borrow(user, book_id):
        borrows = BorrowRepository.read_file()
        borrows.append({
            'id': str(uuid1()),
            'user_id': user.id,
            'book_id': book_id
        })
        BorrowRepository.save_file(borrows)

    @staticmethod
    def get_user_borrows(user_id):
        borrows = BorrowRepository.read_file()
        return [borrow for borrow in borrows if borrow['user_id'] == user_id]

    @staticmethod
    def delete_borrow(user_id, book_id):
        borrows = BorrowRepository.read_file()
        updated = [borrow for borrow in borrows if not (borrow['user_id'] == user_id and borrow['book_id'] == book_id)]
        if len(updated) == len(borrows):
            return False
        BorrowRepository.save_file(updated)
        return True
        