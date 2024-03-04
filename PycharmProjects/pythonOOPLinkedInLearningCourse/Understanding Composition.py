class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []
    def addChapter(self, chapter):
        self.chapters.append(chapter)
    def getBookPagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result
class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f'{self.fname} {self.lname}'
class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", author, 15.99)
b1.addChapter(Chapter("Chapter1", 125))
b1.addChapter(Chapter("Chapter2", 97))
b1.addChapter(Chapter("Chapter3", 143))
print(f'Book title: {b1.title}, author: {b1.author}, pages {b1.getBookPagecount()} -- {b1.price}')