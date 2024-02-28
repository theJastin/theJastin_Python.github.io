# This is a sample Python script.
class Newspaper():
    def __init__(self,name):
        self.name = name
class Book():
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK","EBOOK")

    # private variable
    __booklist = None
    def __init__(self, title, booktype, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # private variable
        self.__secret = "This is a secret attribute"

        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid book type')
        else:
            self.booktype = booktype
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - self.price * self._discount
        else:
            return self.price

    # self - means that is an instance method
    def setDiscount(self, amount):
        self._discount = amount

    # cls - means that is a class method
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # static method (doesn't take any arguments)
    # uses only variables which passed into the method
    def getBooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

book1 = Book("War and Peace", "HARDCOVER","Leo Tolstoy", 1225, 22.99)
book2 = Book("The Catcher in the Rye", "PAPERBACK", "JD Salinger", 381, 15.99)
new1 = Newspaper("Times")
new2 = Newspaper("Seattle Times")

# print(book1.getPrice())
# book1.setDiscount(0.25)
# print(book1.getPrice())
# print(type(new1) == type(new2))
# print(type(book2) == type(book1))

# print(book1._Book__secret)

# print(isinstance(book1, Book))
# print(isinstance(new1, Newspaper))
# print(isinstance(book2, Newspaper))
# print(isinstance(book2, object))

# print(f'Book types: {book1.getBookTypes()}')
thebooks = Book.getBooklist()
print(thebooks)
thebooks.append(book1)
thebooks.append(book2)
print(thebooks)
