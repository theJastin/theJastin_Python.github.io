from abc import ABC

class Asset(ABC):
    def __init__(self, price):
        self.price = price
class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company
    def __str__(self):
        return f'{self.ticker}: {self.company} -- {self.price}'
    def __ge__(self, other):
        if not isinstance(other, Stock):
            raise ValueError("Can't compare a stock with not a stock")
        else:
            return self.price >= other.price
    def __lt__(self, other):
        if not isinstance(other, Stock):
            raise ValueError("Can't compare a stock with not a stock")
        else:
            return self.price < other.price

class Bond(Asset):
    def __init__(self, description, duration, b_yield, price):
        super().__init__(price)

        self.description = description
        self.duration = duration
        self.b_yield = b_yield
    def __str__(self):
        return f'{self.description}: {self.duration}yr : ${self.price} : {self.b_yield}%'
    def __ge__(self, other):
        if not isinstance(other, Bond):
            raise ValueError("Can't compare a bond with not a bond")
        else:
            return self.b_yield >= other.b_yield
    def __lt__(self, other):
        if not isinstance(other, Bond):
            raise ValueError("Can't compare a bond with not a bond")
        else:
            return self.b_yield < other.b_yield

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")
stocks =[msft, goog, meta, amzn]
stocks.sort()
for stock in stocks:
    print([str(stock)])
print('------------------------------')

us30yr = Bond( "30 Year US Treasure", 30, 4.38, 95.31)
us20yr = Bond("20 Year US Treasure", 20, 4.28, 96.41)
us10yr = Bond("10 Year US Treasure", 10, 4.58, 93.15)
us5yr = Bond("5 Year US Treasure", 5, 4.98, 98.4)
bonds = [us30yr, us10yr, us20yr, us5yr]
bonds.sort()
for bond in bonds:
    print([str(bond)])