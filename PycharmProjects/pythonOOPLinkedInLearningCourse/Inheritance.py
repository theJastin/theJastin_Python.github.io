class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)


class Newspaper(Periodical):
    def __init__(self, title, publisher, period, price):
        super().__init__(title, publisher, period, price)


b1 = Book("City of Dragons", "Jaima Yogis", 235, 12.99)
n1 = Newspaper("NY Times", "New York Company", "Daily", 9.99)
m1 = Magazine("Scientific American", "National Geographic", "Monthly", 6.00)

print(f'{b1.title} {b1.author}, {b1.pages} pages -- ${b1.price}')
print(f'{n1.title} {n1.publisher}, {n1.period} pages -- ${n1.price}')
print(f'{m1.title} {m1.publisher}, {m1.period} pages -- ${m1.price}')
