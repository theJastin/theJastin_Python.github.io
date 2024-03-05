from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Asset(ABC):
    price: float

    @abstractmethod
    def __lt__(self, other):
        pass

@dataclass
class Stock(Asset):
    ticker: str
    company: str
    def __lt__(self, other):
        return self.price > other.price
@dataclass
class Bond(Asset):
    description: str
    duration: int
    b_yield: float
    def __lt__(self, other):
        return self.b_yield > other.b_yield

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