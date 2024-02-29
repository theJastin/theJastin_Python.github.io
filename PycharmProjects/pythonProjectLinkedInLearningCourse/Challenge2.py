from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__ (self, price):
        self.price = price
    @abstractmethod
    def getDescription(self):
        pass

class Bond(Asset):
    def __init__(self, description, duration, b_yield, price):
        super().__init__(price)

        self.description = description
        self.duration = duration
        self.b_yield = b_yield

    def getDescription(self):
        return f'{self.description}: {self.duration}yr : Sprice : {self.b_yield}%'
class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def getTicker(self):
        return self.ticker
    def getPrice(self):
        return self.price
    def getCompany(self):
        return self.company
    def getDescription(self):
        return f"{self.getTicker()}: {self.getCompany()} -- ${self.getPrice()}"

try:
    ast = Asset(100.00)
except:
    print("Can't create abstract class object")

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.getDescription())
print(goog.getDescription())
print(meta.getDescription())
print(amzn.getDescription())

us30yr = Bond(95.31, "30 Year US Treasure", 30, 4.38)
us20yr = Bond(96.31, "20 Year US Treasure", 30, 4.28)
us10yr = Bond(94.31, "10 Year US Treasure", 30, 4.58)
us5yr = Bond(98.31, "5 Year US Treasure", 30, 4.98)

print(us30yr.getDescription())
print(us20yr.getDescription())
print(us10yr.getDescription())
print(us5yr.getDescription())