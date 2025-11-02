from classes.book import Book
class User:
    def __init__(self, user_id:str, name:str):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []


    def borrow_book(self,book:Book):
        if book.is_available:
            self.borrowed_books.append(book)
        else:
            print("this book not available")


    def return_book(self,book:Book):
        self.borrowed_books.remove(book)

