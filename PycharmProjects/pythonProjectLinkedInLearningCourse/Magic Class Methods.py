# This is a sample Python script.
class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # return string representation of the class by default
    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'

    # return string representation of the class when called directly
    def __repr__(self):
        return f'title = {self.title}, author = {self.author}, pages = {self.pages}, price = {self.price}'

    # compare two class objects
    def __eq__(self, object):
        if not isinstance(object, Book):
            raise ValueError("Can't compare a book with not a book")
        else:
            return (self.title == object.title and
                    self.author == object.author and
                    self.pages == object.pages and
                    self.price == object.price)

    # check if self greater or equal then object
    def __ge__(self, object):
        if not isinstance(object, Book):
            raise ValueError("Can't compare a book with not a book")
        else:
            return self.price >= object.price

    # check if self less then object
    def __lt__(self, object):
        if not isinstance(object, Book):
            raise ValueError("Can't compare a book with not a book")
        else:
            return self.price < object.price

book1 = Book("War and Peace", "Leo Tolstoy", 1225, 22.99)
book11 = Book("War and Peace", "Leo Tolstoy", 1225, 22.99)
book2 = Book("The Catcher in the Rye", "JD Salinger", 381, 15.99)
book3 = Book("City of Dragons", "Jaima Yogis", 235, 12.99)

# print(str(book1))
# print(repr(book2))

print(book1 == book11)
print(book1 == book2)
#print(book1 == 42)
print(book1 > book11)
print(book1 > book2)

books = [book1, book3, book11, book2]
print([book.title for book in books])
books.sort()
print([book.title for book in books])