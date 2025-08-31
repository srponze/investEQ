from typing import List

import yfinance as yf

from investEQ.model.stock import Stock


class YFinance:

    def getPrices(self, listStocks: List[Stock]):
        for stock in listStocks:
            yfStock = yf.Ticker(stock.ticker)
            price = yfStock.get_fast_info().last_price
            if price is not None:
                stock.price = round(float(price), 4)
            else:
                stock.price = 0.0
