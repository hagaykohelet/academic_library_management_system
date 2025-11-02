from classes.user import User
from classes.book import Book
# from classes.logger import Logger
# from classes.system_admin import SystemAdmin

class Library:
    max_borrow_days = 14

    def __init__(self):
        self.books :dict[str,Book] = {}
        self.users:dict[str,User] = {}

    def register_user(self,user:User):
        self.users[user.user_id] = user.name

    def add_book(self,book:Book):
        self.books[book.isbn] = book.title

    def perform_borrow(self,user_id:str, isbn:str):
        if user_id not in self.users[user_id].user_id:
            raise "your not a library subscriber"

        if isbn not in self.books[isbn].isbn:
            raise "this book not in library"

        book = self.books[isbn]

        if not self.books[isbn].is_available:
            raise f"the {isbn} not available now "


        self.users[user_id].borrowed_books(book)
        book.is_available = False
        Logger.log_action("BORROW",{user_id,isbn})
        SystemAdmin.update_transactions_count()


    def perform_return(self,user_id,isbn):
        if user_id not in self.users[user_id].user_id:
            raise "your not a library subscriber"

        if isbn not in self.books[isbn].isbn:
            raise "this book not in library"

        user = self.users[user_id]
        book = self.books[isbn]

        if self.books[isbn].is_available:
            raise "this book already in library"

        if book not in user.borrowed_books:
            raise "you not borrowed this book"


        user.return_book(book)

        book.is_available = True
        Logger.log_action("RETURN",{user_id,isbn})
        SystemAdmin.update_transactions_count()