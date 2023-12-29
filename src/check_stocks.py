import src.Stockstir.stockstir as Stockstir
#import Stockstir
import time
import sys

stocks = ["GME", "SPY", "MULN", "TTOO", "PBLA", "NKTX", "HUT", "FRGT", "SOXL"]
stock_tuples = []

start_time = time.perf_counter()

stock_prices = Stockstir.Tools.getMultiSymbols(stocks)
stock_changes= Stockstir.Tools.getMultiPercentChanges(stocks)

assert len(stocks) == len(stock_prices) and len(stock_prices) == len(stock_changes), "Unequal number of stocks and properties, probably couldn't retrieve something."

for index, stock in enumerate(stocks):
	stock_tuples.append((stock, stock_prices[index], stock_changes[index]))

for t in stock_tuples:
	print(f'|{t[0]}\t{t[1]}\t{t[2]:.2f}%')

elapsed_time = time.perf_counter() - start_time
