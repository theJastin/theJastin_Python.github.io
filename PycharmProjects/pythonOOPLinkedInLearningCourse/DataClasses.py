from dataclasses import dataclass, field
import random

# returns a random price for a default field price
def price_func():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # setting default value using a function
    price: float = field(default_factory = price_func)

    #using post initialization
    def __post_init__(self):
        self.description = f'{self.title} by {self.author}'

    def bookinfo(self):
        return f'{self.title} by {self.author}'


book1 = Book("War and Peace", "Leo Tolstoy", 1225, 22.99)
book2 = Book("The Catcher in the Rye", "JD Salinger", 381, 15.99)
book3 = Book("War and Peace", "Leo Tolstoy", 1225, 22.99)

# print(book1)
# print(book2)
# print(book1 == book2)
# print(book1 == book3)
# book3.title = "Anna Karenina"
# book3.pages = 845
# book3.price = 18.99
# print(book3.bookinfo())
book4 = Book("Tryout", "Christina Soontornvat", 403)
print(book4)