from classes.user import User
from classes.book import Book
from classes.logger import Logger
from classes.system_admin import SystemAdmin

class Library:
    max_borrow_days = 14

    def __init__(self):
        self.books :dict[str,Book] = {}
        self.users :dict[str,User] = {}

    def register_user(self,user:User):
        self.users[user.user_id] = user

    def add_book(self,book:Book):
        self.books[book.isbn] = book

    def perform_borrow(self,user_id:str, isbn:str):
        if user_id not in self.users.keys():
            raise "your not a library subscriber"

        elif isbn not in self.books.keys():
            raise "this book not in library"



        elif not self.books[isbn].is_available:
            raise f"the {isbn} not available now "

        else:
            book = self.books[isbn]

            self.users[user_id].borrow_book(book)
            book.is_available = False
            Logger.log_action("BORROW",book.isbn)
            SystemAdmin.update_transactions_count()


    def perform_return(self,user_id,isbn):
        if user_id not in self.users.keys():
            raise "your not a library subscriber"

        elif isbn not in self.books.keys():
            raise "this book not in library"



        elif self.books[isbn].is_available:
            raise "this book already in library"

        else:
            user = self.users[user_id]
            book = self.books[isbn]
            if isbn not in user.borrowed_books:
                raise "you not borrowed this book"



            user.return_book(book)

            book.is_available = True
            Logger.log_action("RETURN",book.isbn)
            SystemAdmin.update_transactions_count()