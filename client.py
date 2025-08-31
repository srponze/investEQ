from investEQ.model.stock import Stock
from investEQ.solver import Solver
from investEQ.yfinance import YFinance

cash = 15000.0
margin = 1.005
currency = "$"
listStocks = [
    Stock("AAPL", currency),
    Stock("MSFT", currency),
    Stock("GOOGL", currency),
    Stock("AMZN", currency),
    Stock("TSLA", currency),
    Stock("NFLX", currency),
]

yFinance = YFinance()
yFinance.getPrices(listStocks)

Solver(margin, listStocks, cash, currency)

print("Summary of buys:")
for stock in listStocks:
    print(stock)
