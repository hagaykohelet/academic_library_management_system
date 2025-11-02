from classes.book import Book
from classes.user import User


book1 = Book("hagay","hagay","1243")

user1 = User("segal","hagay")
user1.borrow_book(book1)
print(user1.borrowed_books)

print(book1.get_details())