import time
import random


class Tools:
	# Set some parameters in the class constructor:
	def __init__(self, random_user_agent, print_output):
		self.random_user_agent = random_user_agent
		self.print_output = print_output
	# This first function is solely used in the __init__.py file.
	def set_gather_info(self, gatherinfo):
		self.GatherInfo = gatherinfo
	# The get_single_price function is used to get a single price for a specific ticker/stock symbol, which is the most basic use of Stockstir in general:
	def get_single_price(self, stock_symbol, random_user_agent=None):
		if random_user_agent == None:
			# Set the random_user_agent equal to the one that was passed down in the __init__.py file if it is not passed down in the function:
			random_user_agent = self.random_user_agent
		source = self.GatherInfo.get_source(stock_symbol, random_user_agent=random_user_agent)
		price = self.GatherInfo.gather_price(source)
		return price
	# This is one of the main functions, which gathers multiple data samples for a specific ticker/stock symbol:
	def multi_data_gathering(self, stock_symbol, iterations, break_interval=5, anti_ban=False, random_user_agent=None, print_output=None, return_time_spent=False):
		if random_user_agent == None:
			# Set the random_user_agent equal to the one that was passed down in the __init__.py file if it is not passed down in the function:
			random_user_agent = self.random_user_agent
		if print_output == None:
			# Set the print_output equal to the one that was passed down in the __init__.py file if it is not passed down in the function:
			print_output = self.print_output
		prices = []
		random_delays = []

		for i in range(iterations):
			if anti_ban:
				random_delay = random.randint(50, 100) / 100
				random_delays.append(random_delay)
				time.sleep(random_delay)

			source = self.GatherInfo.get_source(stock_symbol, random_user_agent=random_user_agent)
			price = self.GatherInfo.gather_price(source)
			prices.append(price)

			if print_output:
				print(price)

			if (iterations - 1) != i:
				time.sleep(break_interval)
		# Some logic to determine what to return:
		if return_time_spent and anti_ban:
			time_spent = (iterations * break_interval) + sum(random_delays)
			return prices, time_spent
		elif return_time_spent and not anti_ban:
			time_spent = (iterations * break_interval)
			return prices, time_spent
		else:
			return prices
	# This function just uses the multiDataGathering to returns a list of the prices, rather for each symbol in the passed-down list of symbols:
	def multi_ticker_data_gathering(self, stock_symbols, iterations, break_interval=5, anti_ban=False, random_user_agent=None, print_output=None):
		if random_user_agent == None:
			# Set the random_user_agent equal to the one that was passed down in the __init__.py file if it is not passed down in the function:
			random_user_agent = self.random_user_agent
		if print_output == None:
			# Set the print_output equal to the one that was passed down in the __init__.py file if it is not passed down in the function:
			print_output = self.print_output
		symbol_prices = {}
		for symbol in stock_symbols:
			if print_output:
				print(f"Getting data for {symbol}...")
			symbol_prices[symbol] = self.multi_data_gathering(symbol, iterations, break_interval=break_interval, anti_ban=anti_ban, random_user_agent=random_user_agent, print_output=print_output)
		# Return the dictionary of symbols and prices:
		return symbol_prices
	# This function is used to get the trend of a list of prices, which is used in the multi_data_gathering function:
	def get_trend(self, prices_list, return_change=False):
		trend = ''
		amount_prices = len(prices_list)
		first_price = prices_list[0]
		last_price = prices_list[amount_prices - 1]

		if first_price < last_price:
			trend = 'up'
		elif first_price > last_price:
			trend = 'down'
		else:
			trend = 'neutral'

		if return_change:
			change = float(last_price) - float(first_price)
			return trend, change
		else:
			return trend
	# This function is used to write to a file the data that was gathered using other functions in the library, specificaly the multi_data_gathering function:
	def save_data_to_file(self, data, save_file_path, time_spent=0, trend=''):
		data = str(data)
		save_data_file_name = "stockstirSaveData.txt"
		# Get the path without the last dash (if there is one):
		while True:
			last_character = save_file_path[-1]
			if last_character == "/" or last_character == ' ':
				save_file_path = save_file_path[:-1]
			else:
				break

		f = open(save_file_path + "/" + save_data_file_name, 'a')
		current_time = time.ctime()

		f.write("\n\n" + current_time + "\nData: " + data)

		if time_spent == 0:
			f.write("\nTime Spent: undefined")
		elif time_spent != 0:
			time_spent = str(time_spent)
			f.write("\nTime Spent: " + time_spent)
		if trend == '':
			f.write("\nTrend: undefined")
		elif trend != '':
			f.write("\nTrend: " + trend)
		# Close the file:
		f.close()