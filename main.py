from classes.book import Book
from classes.user import User
from classes.library import Library
from classes.system_admin import SystemAdmin
from classes.logger import Logger

book1 = Book("harry potter1","j.k rowlling","1243")
book2 = Book("harry potter2","hagay","5678")
book3 = Book("harry potter3","j.k rowlling","987")
user1 = User("0123","hagay")
user2 = User("4567","daniel")
user3 = User("987","ary")


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user1)
library.register_user(user2)

print(library.books)
print(library.users)
library.perform_borrow("987","5678")