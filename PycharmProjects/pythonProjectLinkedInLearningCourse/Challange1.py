class Stock():
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    def getTicker(self):
        return self.ticker
    def getPrice(self):
        return self.price
    def getCompany(self):
        return self.company
    def getDescription(self):
        return f"{self.getTicker()}: {self.getCompany()} -- ${self.getPrice()}"

msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")
print(msft.getDescription())
print(goog.getDescription())
print(meta.getDescription())
print(amzn.getDescription())