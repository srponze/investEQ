class Stock:
    def __init__(
        self,
        ticker: str,
        currency: str = "$",
        price: float = 0.0,
        shares: int = 0,
    ):
        self.ticker = ticker
        self.price = price
        self.shares = shares
        self.currency = currency

    def __str__(self):
        return f"{self.ticker:<7} {self.shares:<4} x {str(self.price) + str(self.currency):<8} = {round(self.shares * self.price, 2)}{self.currency}"
