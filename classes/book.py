class Book:
    def __init__(self, title:str, author:str, isbn:str):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True


    def get_details(self):
        return f"teh name of book: {self.title}, the author:{self.author}, the id of book: {self.isbn}, the book in the library: {self.is_available}"


