class Book:
    def __init__(self, title:str, author:str, isbn:str, is_available:bool= True):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available


    def get_details(self):
        return f"teh name of book: {self.title}, the author:{self.author}, the id of book: {self.isbn}, the book in the library: {self.is_available}"


