from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f'{self.title} by {self.author}'


book1 = Book("War and Peace", "Leo Tolstoy", 1225, 22.99)
book2 = Book("The Catcher in the Rye", "JD Salinger", 381, 15.99)
book3 = Book("War and Peace", "Leo Tolstoy", 1225, 22.99)

# print(book1)
# print(book2)
# print(book1 == book2)
# print(book1 == book3)
book3.title = "Anna Karenina"
book3.pages = 845
book3.price = 18.99
print(book3.bookinfo())