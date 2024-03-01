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
        return f'{self.description}: {self.duration}yr : ${self.price} : {self.b_yield}%'

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

us30yr = Bond( "30 Year US Treasure", 30, 4.38, 95.31)
us20yr = Bond("20 Year US Treasure", 20, 4.28, 96.41)
us10yr = Bond("10 Year US Treasure", 10, 4.58, 93.15)
us5yr = Bond("5 Year US Treasure", 5, 4.98, 98.4)

print(us30yr.getDescription())
print(us20yr.getDescription())
print(us10yr.getDescription())
print(us5yr.getDescription())